#!/usr/bin/env python
from scapy.all import *

packets = rdpcap("./capture.pcap")
for pkt in packets[TCP]:
    payload = bytes(pkt[Raw]) if Raw in pkt else b''
    if len(payload) == 16 and payload.isalnum():
        print(f"Possible key in traffic: {payload.decode()}")
