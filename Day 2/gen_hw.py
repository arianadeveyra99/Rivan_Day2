class GenerateItems:
    item_values = {
        'cidr': None,
        'subnet_mask': None,
        'rivan_format': None,
        'wildcard': None,
        'binary_format': None
    }
    
    def __init__(self, total_items):
        self.total_items = total_items
        
        if int(self.total_items) >= 100:
            self.total_items = 100
        
    def gen_item_values(self):
        # Generate items for the exercise
        all_items = {}
        
        for items in range(1, int(self.total_items) + 1):
            GenerateItems.item_values['cidr'] = self.gen_cidr()
            GenerateItems.item_values['subnet_mask'] = self.get_netmask()
            GenerateItems.item_values['rivan_format'] = self.get_rivan_format()
            GenerateItems.item_values['wildcard'] = self.get_wildcard()
            GenerateItems.item_values['binary_format'] = self.get_binary_format()
         
            all_items[str(items)] = self.item_values   
        
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
            
        return bin_value
        
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
    
    new_items = []
    
    def __init__(self, all_items):
        self.all_items = all_items
        
    def prompt_user(self):
        # Prompt the user for their desired given values
        
        cidr_type = 1
        netmask_type = 2
        rivan_type = 3
        wildmask_type = 4
        mixed_type = 5
        
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
            
        if item_type == 1:
            self.cidr_only(self.all_items)
        elif item_type == 2:
            self.net_mask_only(self.all_items)
        elif item_type == 3:
            self.rivan_format_only(self.all_items)
        elif item_type == 4:
            self.wildcard_only(self.all_items)
        elif item_type == 5:
            self.mixed_types(self.all_items)
        else:
            print('Invalid Input.')
        
    def cidr_only(self, all_items):
        
        for items in all_items:
            if items == 'subnet_mask':
                self.all_items[items] = SetItemType.find_mask
            elif items == 'rivan_format':
                self.all_items[items] = SetItemType.find_rivan_format
            elif items == 'wildcard':
                self.all_items[items] = SetItemType.find_mask
                
    def net_mask_only(self, all_items):
        for items in all_items:
            if items == 'cidr':
                self.all_items[items] = SetItemType.find_cidr
            elif items == 'rivan_format':
                self.all_items[items] = SetItemType.find_rivan_format
            elif items == 'wildcard':
                self.all_items[items] = SetItemType.find_mask
                
    def rivan_format_only(self, all_items):
        for items in all_items:
            if items == 'cidr':
                self.all_items[items] = SetItemType.find_cidr
            elif items == 'subnet_mask':
                self.all_items[items] = SetItemType.find_mask
            elif items == 'wildcard':
                self.all_items[items] = SetItemType.find_mask
                
    def wildcard_only(self, all_items):
        for items in all_items:
            if items == 'cidr':
                self.all_items[items] = SetItemType.find_cidr
            elif items == 'rivan_format':
                self.all_items[items] = SetItemType.find_rivan_format
            elif items == 'subnet_mask':
                self.all_items[items] = SetItemType.find_mask
                
    def mixed_types(self, all_items):
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




if __name__ == '__main__':  
    import random
    import socket
    import struct
    import rivan
    
    all_items = GenerateItems(get_total_items()).gen_item_values()
    
    print(all_items)
    
    modify_items = SetItemType(all_items).prompt_user()