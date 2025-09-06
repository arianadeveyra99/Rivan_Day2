import json
import random

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
    
    def random_company(self):
        total_values = len(self.companies)
        chosen_num = random.randint(1, total_values)
        chosen_name = self.companies[chosen_num - 1]

        return(chosen_name)

    def random_user(self):
        total_values = len(self.users)

        max_group = 3
        chosen_name = []

        while max_group > 0:
            chosen_num = random.randint(1, total_values)
            chosen_user = self.users[chosen_num - 1]
            chosen_name.append(chosen_user)

            max_group -= 1

        return(chosen_name)


## Get Company Name
num = RandomSelectValues(company_list, user_list).random_company()
print(num + '.com')

## Get User Groups
users = RandomSelectValues(company_list, user_list).random_user()
print(users)