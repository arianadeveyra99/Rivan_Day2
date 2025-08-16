
<!-- Your monitor number = #$34T# -->


## ⛅ Warm Up for Day 2.
*"Repetition is the mother of all skills"*

<br>

### 🔧 Configure the following:
  - Switch (__CoreTAAS__ & __CoreBABA__)
  - Voice Gateway/Call Manager (__CUCM - Cisco Unified Call Manager__)
  - Router (__EDGE__)

<br>

Verify:

~~~cmd
@cmd
ping 10.91.1.10             PC Network Adapter
ping 10.#$34T#.1.2		    CoreTAAS
ping 10.#$34T#.1.4		    CoreBABA
ping 10.#$34T#.100.8		CUCM
ping 10.#$34T#.#$34T#.1		EDGE - INSIDE
ping 200.0.0.#$34T#		    EDGE - OUTSIDE

ping 200.0.0.k		        Klassmate's EDGE	       k = klassmate's Monitor Number
ping 10.k.100.8		        Klassmate's CUCM
ping 10.k.1.4		        Klassmate's CoreBABA
ping 10.k.1.2		        Klassmate's CoreTAAS
ping 10.k.1.10		        Klassmate's PC
~~~

Your Branch must be able to call other klassmates  

<br>

View your cameras:
  - http://10.#$34T#.50.6
  - http://10.#$34T#.50.8

&nbsp;
---
&nbsp;

### 🌐 Configure DNS
  - Create __DNS zones & records__ for daytwo#$34T#.com  
  - Create a __website__ for daytwo#$34T#.com  
  - Create an __email__ for

| Email                       | Name           |
| ---                         | ---            |
| support@daytwo#$34T#.com    | Rivan Support  |
| user1@daytwo#$34T#.com      | User1          |

<br>

Send an email from support@daytwo#$34T#.com to user1@daytwo#$34T#.com

<br>
<br>

---
&nbsp;

# 💻 Network Fundamentals

<br>

### 🔢 Counting as a network engineer.

|     | Decimal | IPv4          | IPv6   |
| --- | ---     | ---           | ---    |
| -1  | 1999    | 1.255.255.255 | :1fff: |
|     | 2000    | 2.0.0.0       | :2000: |
| +1  | 2001    | 2.0.0.1       | :2001: |
|     |         |               |        |
| -1  |         |               |        |
|     | 2999    | 2.255.255.255 | :2fff: |
| +1  |         |               |        |
|     |         |               |        |
| -1  |         |               |        |
|     | 4099    | 4.0.255.255   | :40ff: |
| +1  |         |               |        |
|     |         |               |        |
| -1  |         |               |        |
|     | 6790    | 6.7.255.0     | :67f0: |
| +1  |         |               |        |
|     |         |               |        |
| -1  |         |               |        |
|     | 5389    | 5.3.8.255     | :538f: |
| +1  |         |               |        |
|     |         |               |        |

&nbsp;
---
&nbsp;

### Internet Protocol Version 4 (IPv4)
*What is the IP address of your phone?*
  - ipchicken.com
  - ipconfig

<br>

### Public IP address
| Class | IP Range                    |
| ---   | ---                         |
| A     | 1.0.0.0 - 126.255.255.255   |
| B     | 128.0.0.0 - 191.255.0.0     |
| C     | 192.0.0.0 - 223.255.255.0   |
| D     | 224.0.0.0 - 239.255.255.255 |
| E     | 240.0.0.0 - 255.255.255.255 |

<br>

~~~cmd
@cmd
ping 8.8.8.8
ping 1.1.1.1
ping 4.4.1.1

tracert 8.8.8.8
~~~

<br>
<br>

<details>
	
~~~cmd
Tracing route to dns.google [8.8.8.8]
over a maximum of 30 hops:

  1    20 ms     1 ms     1 ms  10.28.0.1
  2     2 ms     1 ms     1 ms  192.168.100.1
  3    10 ms    10 ms     8 ms  10.56.0.1
  4     *        9 ms     *     161.49.4.128.convergeict.com [161.49.4.128]
  5     6 ms     4 ms     4 ms  161.49.4.240.convergeict.com [161.49.4.240]
  6     *        *        *     Request timed out.
  7     4 ms     5 ms     5 ms  161.49.6.147.convergeict.com [161.49.6.147]
  8     5 ms     5 ms     4 ms  142.250.174.148
  9     9 ms     5 ms     5 ms  142.251.251.137
 10     5 ms     5 ms     6 ms  142.251.246.167
 11     5 ms     9 ms     4 ms  dns.google [8.8.8.8]
~~~

</details>

&nbsp;
---
&nbsp;

### Private IP address  
*Why do big companies uses the IP addresses that starts with 10.x.x.x ? *

<br>

| Class | IP Range                        | No. of Host |
| ---   | ---                             | ---         |
| A     | 10.0.0.0 - 10.255.255.255       | 16,777,214  |
| B     | 172.16.0.0 - 172.31.255.255     | 64,534      |
| C     | 192.168.0.0 - 192.168.255.255   | 254         |

<br>
<br>
<br>
<br>

---
&nbsp;

## 🙌 CIDR (Rivan Finger Method)
*How do devices see IP addresses? *
	
### `0 0 0 0   0 0 0 0   .   0 0 0 0   0 0 0 0   .   0 0 0 0   0 0 0 0   .   0 0 0 0   0 0 0 0`

<br>
<br>

__Example 01:__
<details>
	
### `1 1 0 0   0 0 0 0   .   1 0 1 0   1 0 0 0   .   0 0 0 1   0 1 0 0   .   0 0 0 0   0 0 0 1`

### `1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   0 0 0 0   0 0 0 0`

<br>
<br>
<br>

### `1 1 0 0   0 0 0 0   .   1 0 1 0   1 0 0 0   .   0 0 0 1   0 1 0 0   .   1 1 1 1   1 1 1 1`

</details>

<br>

__Example 02:__
<details>
	
### `0 0 0 0   1 0 1 0   .   0 1 1 0   0 1 0 0   .   0 0 0 1   0 1 1 0   .   1 1 0 0   1 1 0 1`

### `1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 0 0`

<br>
<br>
<br>

### `0 0 0 0   1 0 1 0   .   0 1 1 0   0 1 0 0   .   0 0 0 1   0 1 1 0   .   1 1 0 0   1 1 1 1`

</details>

<br>

__Example 03:__
<details>
	
### `1 0 1 0   1 1 0 0   .   0 0 0 1   0 0 0 0   .   0 0 1 0   1 0 1 0   .   1 1 0 0   1 1 0 1`

### `1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 1   1 0 0 0   .   0 0 0 0   0 0 0 0`

<br>
<br>
<br>

### `1 0 1 0   1 1 0 0   .   0 0 0 1   0 0 0 0   .   0 0 1 0   1 1 1 1   .   1 1 1 1   1 1 1 1`

</details>

&nbsp;
---
&nbsp;

| Binary             | Decimal|
| ---                | ---    |
| `0 0 0 0  0 0 0 0` | = 0    |
| `0 0 0 0  0 0 0 1` | = 1    |
| `0 0 0 0  0 0 1 0` | = 2    |
| `0 0 0 0  0 0 1 1` | = 3    |
| `0 0 0 0  0 1 0 0` | = 4    |
| `0 0 0 0  0 1 0 1` | = 5    |
| `0 0 0 0  0 1 1 0` | = 6    |
| `0 0 0 0  0 1 1 1` | = 7    |
| `0 0 0 0  1 0 0 0` | = 8    |
| `0 0 0 0  1 0 0 1` | = 9    |
| `0 0 0 0  1 0 1 0` | = 10   |
| `0 0 0 0  1 0 1 1` | = 11   |
| `0 0 0 0  1 1 0 0` | = 12   |
| `0 0 0 0  1 1 0 1` | = 13   |
| `0 0 0 0  1 1 1 0` | = 14   |
| `0 0 0 0  1 1 1 1` | = 15   |
|                    |        |
| `0 0 0 1  0 0 0 0` | = 16   |

<br>
<br>

---
&nbsp;

### 🎯 Exercise 01: Convert CIDR to various formats

<br>

| CIDR | NETMASK     | RIVAN Format | WILDCARD    |
| ---  | ---         | ---          | ---         |
| /20  |             | (Octet, i)   |             |
| /27  |             | (Octet, i)   |             |
| /14  |             | (Octet, i)   |             |

<br>
<br>

---
&nbsp;

## 0️⃣ Bit Length

### `0 0 0 0  0 0 0 0    0 0 0 0  0 0 0 0`

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;

  
### 🎯 Exercise 02: Find the Bit Length

<br>

| Value     | Bits |
| ---       | ---  |
| 195       |      |
| 13        |      |
| 1,750     |      |
| 1,855     |      |
| 2,700     |      |
| 2         |      |
| 376       |      |
| 888       |      |
| 8         |      |
| 212       |      |
| 4,500     |      |
| 81        |      |
| 20,000    |      |
| 55        |      |
| your age  |      |

<br>
<br>

---
&nbsp;


##  Subnetting (Host)

### 🎯 Exercise 03: Design a network for `accenture.com` with 1750 agents, team leads, project managers, and quality assurance teams. Use the 10.0.0.0/8 IP address space.
- [ ] 10.16.0.0/24
- [ ] 10.0.4.0/22
- [ ] 10.0.8.0/21
- [ ] 10.0.32.0/20

<br>
<br>

### CSI Method  
__CONVERT__  
  1750 = 11 bits

<br>

__SUBTRACT__  
  /32 - 11 bits = /21

<br>

<details>

Why /32?  
 
### `0 0 0 0  0 0 0 0  .  0 0 0 0  0 0 0 0  .  0 0 0 0  0 0 0 0  .  0 0 0 0  0 0 0 0`
### `                                                     0 0 0     0 0 0 0  0 0 0 0`
### `_______________________________________________________________________________`
### `0 0 0 0  0 0 0 0  .  0 0 0 0  0 0 0 0  .  0 0 0 0  0                           `

</details>

<br>
	
__INSERT (*IPASOK*)__  
/21 (Octet, i)

<br>

Insert 8 inside the 3rd octet of the given IP address space, 10.0.0.0  

<br>

> __10.0.8.0 /21__

<br>

<details>
	
|                               |                        |
| ---                           | ---                    |
| Network IP                    | 10.0.8.0 255.255.248.0 |
| First Valid (Network +1)      | 10.0.8.1               |
| Last Valid (Broadcast -1)     | 10.0.15.254            |
| Broadcast (Next Network -1)   | 10.0.15.255            |
|                               |                        |
| Next Network (Insert i again) | 10.0.16.0              |

</details>

<br>
<br>

---
&nbsp;

### 🎯 Exercise 04: Design a network for `concentrix.com` with 160 admin, 250 managers, 112 executive, 100 security agents. Use the 172.16.0.0/16 IP address space.
- [ ] 172.16.8.0 /22
- [ ] 172.16.16.0 /23
- [ ] 172.16.4.0 /22
- [ ] 172.16.2.0 /23

<br>

CIA Method
- CONVERT:	
- SUBTRACT:
- INSERT(Ipasok):

<br>

|                               |                        |
| ---                           | ---                    |
| Network IP                    |                        |
| First Valid (Network +1)      |                        |
| Last Valid (Broadcast -1)     |                        |
| Broadcast (Next Network -1)   |                        |
|                               |                        |
| Next Network (Insert i again) |                        |

<br>
<br>

---
&nbsp;

### 🎯 Exercise 05: Design and implement a network for `foundever.com` with 45 users. Use the 192.168.0.0/24 IP address space
CIA Method
- CONVERT:	
- SUBTRACT:
- INSERT(Ipasok):

<br>

|                               |                        |
| ---                           | ---                    |
| Network IP                    |                        |
| First Valid (Network +1)      |                        |
| Last Valid (Broadcast -1)     |                        |
| Broadcast (Next Network -1)   |                        |
|                               |                        |
| Next Network (Insert i again) |                        |

<br>
<br>

__IMPLEMENTATION__

~~~
config t
 vlan 25
  name _____.com
  exit
 int vlan 25
  no shut
  ip add __.__.__.__  __.__.__.__
 ip dhcp excluded-add __.__.__.__  __.__.__.__
 ip dhcp pool _____.com
  network __.__.__.__  __.__.__.__
  default-router __.__.__.__
  domain-name _____.com
  dns-server 10.#$34T#.1.10
  option 150 ip 10.#$34T#.100.8
 int fa 0/5
  switchport voice vlan 25
  end
show ip dhcp binding
~~~

<br>
<br>

---
&nbsp;


### 🎯 Exercise 06: Design and implement networks.
P1
- IP address: 10.35.0.0/16
- Domain Name: BSP.COM
- Number of Users: 812
- Reserved IPs: First 70 IPs
- Assign to VLAN: 35

<br>

P1
- IP address: 172.16.87.0/16
- Domain Name: ACCENTURE.COM
- Number of Users: 87
- Reserved IPs: First 10 IPs
- Assign to VLAN: 40

<br>

S1
- IP address: 192.168.52.0/24
- Domain Name: TELETECH.NET
- Number of Users: 345
- Reserved IPs: First 100 IPs
- Assign to VLAN: 52
	
<br>

S2
- IP address: 10.67.0.0/16
- Domain Name: FOUNDEVER.COM
- Number of Users: 1456
- Reserved IPs: First 100 IPs
- Assign to VLAN: 67

<br>
<br>

---
&nbsp;

## Subnetting (Subnet)

### `0 0 0 0   1 0 1 0   .   0 0 1 0   0 0 1 0   .   1 0 0 0   0 0 0 0   .   0 0 0 0   0 0 0 0`

### `1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 0 0   0 0 0 0   .   0 0 0 0   0 0 0 0`

<br>
<br>

### Subnet for 8 offices using the Network address 192.168.128.0/27  Maximize the number of IP addresses.

### `1 1 0 0   0 0 0 0   .   1 0 1 0   0 1 0 0   .   1 0 0 0   0 0 0 0   .   0 0 0 0   0 0 0 0`

### `1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 0   0 0 0 0`

### CAI Method  
__CONVERT *(Bit Value. NOT Length)*__
  8 = 3 bits

<br>

__ADD__
  /27 + 3 bits = /30 (4th, 4i)

<br>

__INSERT(*IPASOK*)__
  1st Office: 192.168.128.0 /30
  2nd Office: 192.168.128.4 /30
  3rd Office: 192.168.128.8 /30
  4th Office: 192.168.128.12 /30
  5th Office: 192.168.128.16 /30
  6th Office: 192.168.128.20 /30
  7th Office: 192.168.128.24 /30
  8th Office: 192.168.128.28 /30
  
  9th Office: 192.168.128.32 /30
	
	From the network 192.168.128.0 /27 (4th, 32i)
	Valid Range:
		First Valid: 192.168.128.1 /27
		Last Valid 192.168.128.30 
		Broadcast: 192.168.128.31
	
	Next Network: 192.168.128.32 /27


Ex. 2 Subnet for 20 offices using the Network address 172.16.225.0/19. 
Maximize the number of IP addresses.




Ex. 3 Subnet for 20 offices using the Network address 172.16.225.0/19. 
Maximize the number of IP addresses.






