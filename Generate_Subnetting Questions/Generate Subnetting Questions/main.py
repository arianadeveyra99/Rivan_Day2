import json
import random
import ipadd
import pprint
import rivan

with open('names.json') as file:
    name_store = json.load(file)

company_list = name_store['Company_Names']
user_list = name_store['User_Groups']

# INIT VARS
## Given Values
company_name = None
req_hosts = None
user_group = None
ip_space = None
req_reserved_ips = None
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

class Computation:
    def __init__(self, companies, users, is_question=True):
        self.companies = companies
        self.users = users
        self.is_question = is_question
    
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

            if chosen_user in chosen_name:
                pass
            else:
                if max_group == 1:
                    chosen_name.append('and ' + chosen_user)
                else:
                    chosen_name.append(chosen_user)
                max_group -= 1

        return chosen_name
    
    def rand_net(self):
        # Pick a random private network address
        private_ranges = [
            ipadd.IPv4Network("10.0.0.0/8"),
            ipadd.IPv4Network("172.16.0.0/12"),
            ipadd.IPv4Network("192.168.0.0/16"),
        ]
        
        while True:
            try:
                base = random.choice(private_ranges)
                
                # Pick a random _prefix length between /4 and /30
                _prefix = random.randint(4, 30)

                if base == ipadd.IPv4Network("10.0.0.0/8"):
                    # Pick a random _prefix length between /4 and /30
                    _prefix = random.randint(9, 30)

                elif base == ipadd.IPv4Network("172.16.0.0/12"):
                    # Pick a random _prefix length between /12 and /30
                    _prefix = random.randint(17, 30)
                
                elif base == ipadd.IPv4Network("192.168.0.0/16"):
                    # Pick a random _prefix length between /16 and /30
                    _prefix = random.randint(25, 30)

                subnets = list(base.subnets(new_prefix=_prefix))

            except:
                continue
            else:
                break

        ## NETWORK: Select a random subnet
        total_subnets = len(subnets)
        chosen_subnet = random.randint(1, total_subnets - 2)
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

        ## Get total HOSTS
        _hosts = len(list(_network)) - 2

        network_values = {
            'prefix': _prefix,
            'increment': _i,
            'hosts': _hosts,
            'network': _network,
            'first_valid': _first_valid,
            'last_valid': _last_valid,
            'broadcast': _broadcast,
            'next_network': _next_network
        }
        
        if self.is_question == True:
            if _hosts > 6000:
                _hosts = 6000

            _given_req_hosts = random.randint(2, _hosts)
            _given_reserved_ips = self.set_reserved_ips(_given_req_hosts)

            _given_values = {
                'network': _network,
                'req_hosts': _given_req_hosts,
                'reserved_ips': _given_reserved_ips
            }

            return _given_values

        return network_values
    

    def set_reserved_ips(self, req_hosts):
        ip_res = int(0.2*req_hosts)
        
        if ip_res > 1_000:
            ip_res = 200

        elif ip_res > 200:
            ip_res = 100

        elif ip_res > 100:
            ip_res = 50

        elif ip_res > 50:
            ip_res = 10

        elif ip_res > 10:
            ip_res = 4

        else:
            ip_res = 2
        
        return (ip_res)
    
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


## Given Company
company = Computation(company_list, user_list).rand_company()
company_name = company + '.com'

## Given User Groups
user_group = Computation(company_list, user_list).rand_user_groups()
user_group = str(user_group).replace('\'', '')
user_group = str(user_group).replace('[', '')
user_group = str(user_group).replace(']', '')

## Given VLAN
vlan = Computation(company_list, user_list).rand_vlan()

## Given IP Address Space
req_values = Computation(company_list, user_list).rand_net()
ip_space = str(req_values['network'])

## Given Required Hosts
req_hosts = req_values['req_hosts']

## Given Required Reserved IPs
req_reserved_ips = req_values['reserved_ips']

## Question
question_temp = f'''
Design a network for {company_name} with {req_hosts} {user_group}. 
- Use the available IP address space {ip_space}
- Reserve the first {req_reserved_ips} IP addresses of the network.
- Set the network for VLAN {vlan}
'''

print(f'''
-----------QUESTION------------
{question_temp}
      ''')


## Solution
host_bits = rivan.GetCAI(req_hosts).convert_host_bits()
constant = 32
new_slash = f'/{str(constant - host_bits)}' 
rivan_format = rivan.FromCIDR.to_rivan(new_slash)

print(f'''
      Convert: {req_hosts} = {host_bits} bits
      Subtract: {constant} - {host_bits} = {new_slash} = ({rivan_format})
      Ipasok: Ipasok
      ''')

## Answer
answer_temp = f'''
C: {req_hosts} = {host_bits} bits

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

# print(answer_temp)
