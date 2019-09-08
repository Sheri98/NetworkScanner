#! /usr/bin/env python

import scapy.all as scapy 
import optparse

def setting():
	parser = optparse.OptionParser()
	parser.add_option("-i","--ip",dest="ip",help="specify your ip")
	(options,arguments)	= parser.parse_args()
	if not options.ip:
		parse.error("Specifiy the ip or ip range") 
	return options
	
 


def scan(ip):
	arp_request   = scapy.ARP(pdst=ip)
	broadcast     = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_brd   = broadcast/arp_request
	ans           = scapy.srp(arp_req_brd,timeout = 1,verbose=False)[0]
	print("	" + "-"*42)
	print("	" + "IP" + "	"*3 + "MAC ADDRESS")
	print(" 	" + "-"*42)
	for i in ans:
		print("	" + i[1].psrc + "	"*2+  i[1].hwsrc)
		
options =  setting()
scan(options.ip)
