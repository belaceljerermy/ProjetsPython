from scapy.all import *
import sys


interface = "eth1"

pk = Ether(src=RandMAC("*:*:*:*:*:*"), dst=RandMAC("*:*:*:*:*:*"))/IP(src=RandIP("*.*.*.*"), dst=RandIP("*.*.*.*"))/ICMP()
print pk.display()

    sendp(pk, interface, loop = 1)
print "exiting"
sys.exit(0)

