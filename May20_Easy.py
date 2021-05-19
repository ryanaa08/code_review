"""EASY
 From a list of IP addresses, return the first index and the last index in the list. Also return the number of 
 available hosts in your network. 
 *** Networks can be chosen at random, or you can use the example network below ***
 Ex. 
['192.168.0.0', '192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5', '192.168.0.6', '192.168.0.7']
 
192.168.0.0
192.168.0.7
6 hosts in this range"""

## Create list of IP Addresses ##

IP_list = ['192.168.0.0', '192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5', '192.168.0.6', '192.168.0.7']

## Calculate the number of hosts in the index

host_number = len(IP_list)

print(IP_list[0])
print(IP_list[6])
print ('Number of hosts:', host_number)