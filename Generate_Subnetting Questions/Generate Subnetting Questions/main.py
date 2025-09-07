import json
import random
import ipadd
import pprint
import rivan

with open('names.json') as file:
    name_store = json.load(file)

company_list = name_store['Company_Names']
user_list = name_store['User_Groups']

## Given Values
company_name = None
total_users = None
#user_list = None
ip_space = None
reserved_ip = None
vlan = None

## Answers
host_bits = None
new_net_bits = None
new_cidr = None

rivan_format = None
increment = None
octet = None

company_net_ip = None
company_net_mask = None

first_valid = None
last_valid = None
broadcast = None

not_net_ip = None
not_net_mask = None

question_temp = f'''
Design a network for {company_name} with {total_users} {user_list}. 
- Use the available IP address space {ip_space}
- Reserve the first {reserved_ip} IP addresses of the network.
- Set the network for VLAN {vlan}
'''

answer_temp = f'''
C: {total_users} = {host_bits} bits

S: /32 - {host_bits} = {new_cidr} {rivan_format}

I: Ipasok {increment} sa {octet} octet = {company_net_ip} {company_net_mask}

--

NETWORK: ({company_name}) = {company_net_ip} {company_net_mask}
VALID RANGE:
- FIRST VALID IP = {first_valid}
- LAST VALID IP = {last_valid}
BROADCAST/LAST IP = {broadcast}

NOT NETWORK: (NOT {company_name}) = {not_net_ip} {not_net_mask}
'''

class RandomSelectValues:
    def __init__(self, companies, users):
        self.companies = companies
        self.users = users
    
    def rand_company(self):
        total_values = len(self.companies)
        chosen_num = random.randint(1, total_values)
        chosen_name = self.companies[chosen_num - 1]

        return chosen_name

    def rand_user_groups(self):
        total_values = len(self.users)

        max_group = 3
        chosen_name = []

        while max_group > 0:
            chosen_num = random.randint(1, total_values)
            chosen_user = self.users[chosen_num - 1]
            chosen_name.append(chosen_user)

            max_group -= 1

        return chosen_name
    
    def rand_total_users(self):
        total_users = random.randint(1, 2000)
        
        ip_res = int(0.2*total_users)
        
        if ip_res > 2000:
            ip_res = 2000
        elif ip_res > 1000:
            ip_res = 1000
        elif ip_res > 500:
            ip_res = 500
        elif ip_res > 100:
            ip_res = 100
        elif ip_res > 60:
            ip_res = 60
        else:
            ip_res = 10
        
        return (total_users, ip_res)
    
    def rand_vlan(self):
        set_vlan = random.randint(1, 200)
        
        return (set_vlan)
    
    # def rand_ip(self):
    #     random_int = random.randint(0, 2**32 - 1)
    #     random_ip = ipadd.IPv4Address(random_int)
        
    #     # Generate a random _prefix length.
    #     random__prefix = random.randint(1, 32)
        
    #     # Combine into a network object.
    #     random_network = ipadd.IPv4Network(f"{random_ip}/{random__prefix}", strict=False)
        
    #     return (random_network, random_ip)
        
    def rand_net(self):
        # Pick a random private network address
        private_ranges = [
            ipadd.IPv4Network("10.0.0.0/8"),
            ipadd.IPv4Network("172.16.0.0/12"),
            ipadd.IPv4Network("192.168.0.0/16"),
        ]
        base = random.choice(private_ranges)
        
        # Pick a random _prefix length between /4 and /30
        _prefix = random.randint(4, 30)

        if base == ipadd.IPv4Network("10.0.0.0/8"):
            # Pick a random _prefix length between /4 and /30
            _prefix = random.randint(8, 30)

        elif base == ipadd.IPv4Network("172.16.0.0/12"):
            # Pick a random _prefix length between /12 and /30
            _prefix = random.randint(16, 30)
        
        elif base == ipadd.IPv4Network("192.168.0.0/16"):
            # Pick a random _prefix length between /16 and /30
            _prefix = random.randint(24, 30)

        subnets = list(base.subnets(new_prefix=_prefix))

        
        ## NETWORK: Select a random subnet
        total_subnets = len(subnets)
        chosen_subnet = random.randint(1, total_subnets - 1)
        _network = subnets[chosen_subnet]

        ## NOT NETWORK: Determine the next network
        _next_network = subnets[chosen_subnet + 1]

        ## Get the increment
        _i = rivan.FromCIDR.get_inc(_prefix)

        ## Get valid range
        ## FIRST VALID IP
        _first_valid = _network[1]

        ## LAST VALID IP
        _last_valid = _network[-2]

        
        ## LAST IP/BROADCAST
        _broadcast = _network[-1]

        network_values = {
            'prefix': _prefix,
            'increment': _i,
            'network': _network,
            'first_valid': _first_valid,
            'last_valid': _last_valid,
            'broadcast': _broadcast,
            'next_network': _next_network
        }

        pprint.pp(network_values)

        return network_values

## Get Company Name
num = RandomSelectValues(company_list, user_list).rand_company()
# print(num + '.com')

## Get User Groups
group_users = RandomSelectValues(company_list, user_list).rand_user_groups()
# print(group_users)

## Get Number of Users
num_users = RandomSelectValues(company_list, user_list).rand_total_users()
# print(num_users)

## Get VLAN
vlan = RandomSelectValues(company_list, user_list).rand_vlan()
# print(vlan)

## Get IP address space
ipv4_add = RandomSelectValues(company_list, user_list).rand_net()
# pprint.pp(ipv4_add)

# ## Get Random IPs
# ipv4_set = RandomSelectValues(company_list, user_list).rand_ip()
# print(ipv4_set)
