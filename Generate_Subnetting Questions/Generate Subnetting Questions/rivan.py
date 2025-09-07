# Rivan Format = (Octet, Increment)

class FromCIDR:
    def __init__(self):
        pass
        
    def get_oct(cidr):
        # Determine the Octet
        
        if cidr <= 8:
            octet = '1st'
        elif cidr <= 16:
            octet = '2nd'
        elif cidr <= 24:
            octet = '3rd'
        elif cidr <= 32:
            octet = '4th'
        
        return octet

    def get_inc(cidr):
        # Determine the Increment
        
        _64i = (2,10,18,26)
        _32i = (3,11,19,27)
        _16i = (4,12,20,28)
        _8i = (5,13,21,29)
        _4i = (6,14,22,30)
        _2i = (7,15,23,31)
        _1i = (8,16,24,32)
        
        if cidr in _1i:
            increment = 1
        elif cidr in _2i:
            increment = 2
        elif cidr in _4i:
            increment = 4
        elif cidr in _8i:
            increment = 8
        elif cidr in _16i:
            increment = 16
        elif cidr in _32i:
            increment = 32
        elif cidr in _64i:
            increment = 64
        else:
            increment = 128
        
        return increment
    
    def to_rivan(cidr):
        octet = FromCIDR.get_oct(cidr)
        increment = FromCIDR.get_inc(cidr)
        
        return f'({octet}, {str(increment)}i)'

class GetCAI:
    def __init__(self, given_hosts):
        self.given_hosts = int(given_hosts)
    
    def convert_host_bits(self):
        if self.given_hosts >= 32768:
            host_bits = 16
        elif self.given_hosts >= 16384:
            host_bits = 15
        elif self.given_hosts >= 8192:
            host_bits = 14
        elif self.given_hosts >= 4096:
            host_bits = 13
        elif self.given_hosts >= 2048:
            host_bits = 12
        elif self.given_hosts >= 1024:
            host_bits = 11
        elif self.given_hosts >= 512:
            host_bits = 10
        elif self.given_hosts >= 256:
            host_bits = 9
        elif self.given_hosts >= 128:
            host_bits = 8
        elif self.given_hosts >= 64:
            host_bits = 7
        elif self.given_hosts >= 32:
            host_bits = 6
        elif self.given_hosts >= 16:
            host_bits = 5
        elif self.given_hosts >= 8:
            host_bits = 4
        elif self.given_hosts >= 4:
            host_bits = 3
        elif self.given_hosts >= 2:
            host_bits = 2
        elif self.given_hosts >= 1:
            host_bits = 1
        
        return host_bits
        
        
        
        
        
        
