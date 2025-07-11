class GenerateItems:
    def __init__(self, total_items):
        self.total_items = total_items
        
        if int(self.total_items) >= 100:
            self.total_items = 100
        
    def gen_item_values(self):
        # Generate items for the exercise
        all_items = {}
        item_values = {}
        item_values['cidr'] = self.gen_cidr()
        item_values['subnet_mask'] = self.get_netmask()
        item_values['rivan_format'] = self.get_rivan_format()
        item_values['wildcard'] = self.get_wildcard()
        item_values['binary_format'] = self.get_binary_format()
        
        all_items[str(self.total_items)] = item_values   
        
        
        return all_items
    
    def gen_cidr(self):
        # Randomly generate a number to use as the CIDR
        
        self.random_cidr = random.randint(1,32)
        cidr_value = f'/{str(self.random_cidr)}'
        
        return cidr_value
    
    def get_netmask(self):
        # Determines the subnet mask of the cidr.
        
        net_bits = 32 - self.random_cidr
        self.netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << net_bits)))
        
        return self.netmask
    
    def get_rivan_format(self):
        # Determine the rivan format of the cidr
        
        rivan_format = rivan.FromCIDR.to_rivan(self.random_cidr)
        
        return rivan_format
    
    def get_wildcard(self):
        # Determine the wildcard of the cidr
        
        self.per_octet = self.netmask.split('.')
        bin_value = []
        
        for decimal in self.per_octet:
            difference = 255 - int(decimal)
            bin_value.append(difference)
            
        return str(bin_value)
        
    def get_binary_format(self):       
        # Determine the binary formate of the cidr
        
        self.per_octet = self.netmask.split('.')
        bin_value = []
        
        for decimal in self.per_octet:
            bin_form = format(int(decimal), f'0{8}b')
            bin_value.append(bin_form)
            
        to_bits = f'{bin_value[0]} . {bin_value[1]} . {bin_value[2]} . {bin_value[3]}'
        
        return to_bits

class SetItemType:
    find_cidr = '/?'
    find_mask = '___.___.___.___'
    find_rivan_format = '(Octet, i)'
    find_bin = '00000000 . 00000000 . 00000000 . 00000000'
    
    new_items = []
    
    def __init__(self, all_items):
        self.all_items = all_items
        
    def prompt_user(self, prompt=False, set_type=None):
        # Prompt the user for their desired given values
        self.prompt = prompt
        self.set_type = set_type
        
        item_type = None
        cidr_type = 1
        netmask_type = 2
        rivan_type = 3
        wildmask_type = 4
        mixed_type = 5
        
        if self.prompt:
            while True:
                item_type = input('''
What will be the given value for the exercise? 
    CIDR = 1
    Subnet Mask = 2
    Rivan Format = 3
    Wildcard = 4
    Mixed Values = 5

> ''')
                try:
                    int(item_type)
                    break
                except ValueError:
                    print('Invalid Input. Enter a number. ')
        
            item_type = int(item_type)
        else: 
            pass
            
        if item_type == cidr_type or set_type == cidr_type:
            self.output = self.cidr_only(self.all_items)
            
        elif item_type == netmask_type or set_type == netmask_type:
            self.output = self.net_mask_only(self.all_items)
            
        elif item_type == rivan_type or set_type == rivan_type:
            self.output = self.rivan_format_only(self.all_items)
            
        elif item_type == wildmask_type or set_type == wildmask_type:
            self.output = self.wildcard_only(self.all_items)
            
        elif item_type == mixed_type or set_type == mixed_type:
            self.output = self.mixed_types(self.all_items)
            
        else:
            print('Invalid Input.')
        
        return self.output
        
    def cidr_only(self, all_items):
        self.all_items = all_items
        
        for items in self.all_items:
            for per in items:
                for pi in items[per]:
                    if pi == 'subnet_mask':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_mask
                    elif pi == 'rivan_format':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_rivan_format
                    elif pi == 'wildcard':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_mask
                    elif pi == 'binary_format':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_bin
        
        return self.all_items
                
    def net_mask_only(self, all_items):
        self.all_items = all_items
        
        for items in self.all_items:
            for per in items:
                for pi in items[per]:
                    if pi == 'cidr':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_cidr
                    elif pi == 'rivan_format':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_rivan_format
                    elif pi == 'wildcard':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_mask
                    elif pi == 'binary_format':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_bin
        
        return self.all_items
                
    def rivan_format_only(self, all_items):
        self.all_items = all_items
        
        for items in self.all_items:
            for per in items:
                for pi in items[per]:
                    if pi == 'cidr':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_cidr
                    elif pi == 'subnet_mask':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_mask
                    elif pi == 'wildcard':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_mask
                    elif pi == 'binary_format':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_bin
        
        return self.all_items
                
    def wildcard_only(self, all_items):
        self.all_items = all_items
        
        for items in self.all_items:
            for per in items:
                for pi in items[per]:
                    if pi == 'cidr':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_cidr
                    elif pi == 'rivan_format':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_rivan_format
                    elif pi == 'subnet_mask':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_mask
                    elif pi == 'binary_format':
                        self.all_items[self.all_items.index(items)][per][pi] = SetItemType.find_bin
        
        return self.all_items
                
    def mixed_types(self, all_items):
        self.all_items = all_items
        
        item_count = len(self.all_items)
        print(item_count)
        pass
  
def get_total_items():
    # Prompt the user for the number of items in the exercise.
    
    total = None
    
    while True:
        total = input('How many items for the exercise? ')
        try:
            int(total)
            break
        except ValueError:
            print('Invalid Input. Enter a number. ')
    
    return total

def gen_many(total):
    value = []
    for items in range(1, int(total) + 1):
        num = GenerateItems(items).gen_item_values()
        value.append(num)
    
    return value
    


if __name__ == '__main__':  
    import random
    import socket
    import struct
    import rivan
    import json
    
    unansw = []
    ans = []
    
    for set in range(1, 5):
        all_items = gen_many(3) 
        
        ans.append(all_items)

    with open('test_answers.json', 'w') as file:
        output = json.dumps(ans, indent=4)
        file.write(output)
    
    set = 0
    for i in ans:
        set += 1
        modify_items = SetItemType(i).prompt_user(False, set)
        unansw.append(modify_items)
    
    with open('test.json', 'w') as file:
        output = json.dumps(unansw, indent=4)
        file.write(output)
