"""MEDIUM
From the easy challenge, write a Python script to subnet a network size of your choice. 
Return whether this network is public or private"""


## Import NetAddr for subnetting and pprint for formatting##

from netaddr import *
import pprint
from ipaddress import IPv4Address

## Create variable ip_host without cidr, and create variable ip using the IPNetwork Object##

ip_host = ('192.168.0.1')
ip = IPNetwork('192.168.0.0/24')

## Using module subnet calculate the subnet for 192.169.0.0 /24 using subnet mask /26 and convert to a list ##

subnets = list(ip.subnet(26))
pprint.pprint(subnets)

## Check to see if IP Address it public of private using module from ipaddress##

if IPv4Address(ip_host).is_private == True:
    print('Private')
else:
    print('Public')




