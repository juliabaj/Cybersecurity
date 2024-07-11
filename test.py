from scapy.all import *

def print_pkt(pkt):
    pkt.show()

print("Sniffing packets...")
sniff(prn=print_pkt)
