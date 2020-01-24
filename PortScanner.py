import re
import socket
import os
import subprocess
from ipaddress import ip_address
import sys
from datetime import datetime
#import netaddr
import contextlib
#Target = input("Enter host to scan: ")
#ServerIP = socket.gethostbyname(Target)

w_list=[]
P_list=[]
ip_list=[]
KnownList=[1, 5, 7, 18, 20, 21, 22, 23, 25, 29, 37, 42, 43, 49, 53, 69, 70, 79, 80, 103, 108, 109, 110, 115, 118, 119, 137, 139, 143, 150, 156, 161, 179, 190, 194, 197, 389, 396, 443, 444, 445, 458, 546, 547, 563, 569, 1080]

def checkIp(ipS,ipE):
	if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ipS) and re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ipE):
		return (ipS,ipE)
	else:
 		print("\n ERROR!! InValid Range or IP\n")
 		sys.exit()

def checkPort(portStart,portEnd):
	if re.match(r"\d{1,5}$",portStart) and re.match(r"\d{1,5}$",portEnd):
		portStart, portEnd = [int(portStart), int(portEnd)]
		for i in range (portStart,portEnd+1):
			P_list.append(i)
		return (P_list)
	else:
		print("Error!!! InValid Port_Range ")
		sys.exit() 	
def ips(start, end):
    start_ip = int(ip_address(start))
    end_ip = int(ip_address(end))+1
    return [ip_address(ip).exploded for ip in range(start_ip,end_ip)]		
def Scan(list1,user_List):
	try:
		print ('\n \t \t \t ... Start SCANNING on hosts ...')
		for host in list1:
 			response = subprocess.Popen("ping -c 2 " + host,shell=True,stdout=subprocess.PIPE).stdout.read()
 			if ('ttl' in str(response)):
 				print (host,"is up ")
 				print('------------------')
 				print ("PORT  STATE SERVICE VERSION ")
 				for port in user_List:
 					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 					s.settimeout(10)
 					result = s.connect_ex((host, port))
 					if result==0:
 						# print("port",port,"is open\n")
 						tcpnmap = subprocess.Popen("nmap -sV -sC -p "+str(port)+" "+str(host),shell=True, 		stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
 						res  = str(tcpnmap.stdout.read())
 						Final_res=res.split("\\n")
 						print(str(Final_res[5]))
 						s.close()
 			else:
 				print(host,"is down :( \n")			
	except KeyboardInterrupt:
 		print("SCANNING Interrruped")
 		sys.exit()


def main():
	# ipStart, ipEnd = input ("Enter FirstIP-LastIP:").split("-")
	print("\t\t\t\t Welcome To 3WAD MAP :)\n ")
	ipStart = input("Enter FirstIP >> ")
	ipEnd = input  ("Enter LastIp  >> ")

	ip_list=checkIp(ipStart,ipEnd)
	list1=ips(ipStart,ipEnd)
	user_I=input("\nPress '1' to Scan on KnownPorts Press '2' For Enter YourRange >> ")
	if (user_I)=='2':
		portStart = input ("\nEnter First_Port >> ")
		portEnd = input   ("Enter Last_Port  >> ")
		P_list=checkPort(portStart,portEnd)
		Press = input("\n Press '1' to print on Screen or '2' save output to file>>  ")
		if Press=='1':
			t1=datetime.now()
			Scan(list1,P_list)
		elif Press=='2':
			print("\n\t \t ................ Start Scanning ,, Wait.............. \n")
			f=open('3wadMap.txt','w')
			print("")
			t1=datetime.now()
			with contextlib.redirect_stdout(f):
				Scan(list1,P_list)

	elif (user_I=='1'):
		Press = input("Press '1' to print on Screen or '2' save output to file>>  ")
		if Press=='1':
			t1=datetime.now()
			Scan(list1,KnownList)
		elif Press=='2':
			print("\n\t \t ................ Start Scanning , Wait .............. \n")
			f=open('3wadMap.txt','w')
			print("")
			t1=datetime.now()
			with contextlib.redirect_stdout(f):
				Scan(list1,KnownList)
	#hosts=['104.36.195.224','127.0.0.1']
	t2=datetime.now()
	timeTotal=t2-t1
	print("\nYour Scan Has been Finished and Report saved successfully to '3wadMap.txt' if u choose save output \n ","\n*TimeTaken* " , timeTotal)
