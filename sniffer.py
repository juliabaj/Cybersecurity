from scapy.all import sniff, Dot11, Dot11ProbeReq
interface = 'wlan0'
probeReqs= []

def sniffer(p):
	if p.haslayer(Dot11ProbeReq):
		netName = p.getlayer(Dot11ProbeReq).info.decode()
		print(f"Detected probe request: {netName}")
		if netName not in probeReqs:
			probeReqs.append(netName)
			print('[+] Detected new probe request: ' +netName)
		

print(f"Sniffing on intereface {interface}...")
sniff(iface=interface, prn=sniffer)
print("Sniffing complete")
