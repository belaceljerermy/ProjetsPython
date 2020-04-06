import socket
from scapy.all import *


macsrc = "00:12:b4:e2:f6:c4"
macdst = "52:54:00:12:35:00"
packet = Ether(src=macsrc, dst=macdst)/IP(dst="10.0.2.1", src="10.0.2.3")/TCP(dport=80, flags='S')
sendp(packet)
