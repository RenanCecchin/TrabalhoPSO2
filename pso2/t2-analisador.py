import sys
import csv
import re
from collections import Counter

from time import sleep

try:
    file = sys.argv[1]
except:
	print("Missing the file in the instruction")
	sys.exit()


def packagesNumber():
	packages = 0
	print("Counting the number of packages:")
	txt =open(file)
	for line in txt:
		packages+=1
	print("This file has %d packages\n" %packages)

def sourceIP():
	print("Sorting by top 10 Source IPs:")
	iplist = Counter()
	txt = open(file, 'r')
	for line in txt:
		ipsrc = re.findall('SRC=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
		iplist.update(ipsrc)
	for x in iplist.most_common(10):
		print(x[0][4:] + " has " + str(x[1]) + " packages")
	print("\n")
			
def destinationIP():
	print("Sorting by top 10 Destination IPs:")
	iplist = Counter()
	txt = open(file, 'r')
	for line in txt:
		ipdst = re.findall('DST=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
		iplist.update(ipdst)
	for x in iplist.most_common(10):
		print(x[0][4:] + " has " + str(x[1]) + " packages")
	print("\n")

def protocol():
	print("Counting packages by protocol:")
	protolist = Counter()
	txt = open(file, 'r')
	for line in txt:
		protodst = re.findall('PROTO=[A-Z]{1,4}', line)
		protolist.update(protodst)
	for x in protolist.most_common(10):
		print("Using "+ x[0][6:] + " protocol in " + str(x[1]) + " packages")
	print("\n")

def port():
	print("Counting packages by port:")
	portlist = Counter()
	txt = open(file, 'r')
	for line in txt:
		portdst = re.findall('DPT=[0-9]{1,4}', line)
		portsrc = re.findall('SPT=[0-9]{1,3}', line)
		try:
			portdst[0] = portdst[0][4:]
			portsrc[0] = portsrc[0][4:]
		except:
			pass
		portlist.update(portdst)
		portlist.update(portsrc)
	for x in portlist.most_common(10):
		print("Using port "+ x[0] + " in " + str(x[1]) + " packages\t")
	print("\n")

packagesNumber()
sourceIP()
destinationIP()
protocol()
port()