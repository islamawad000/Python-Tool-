import re
import sys 

def main():
		
	ff=open("logs.txt","r").readlines()
	logs = []
	Pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
	Pattern2=re.compile(r'GET|POST')
	Pattern3=re.compile(r'(\s\/.+?\s)')
	Pattern4=re.compile(r'([a-z[A-z]+/[0-9].[0-9]+\s.+[0-9])')

	try:
		
		for i in ff:
			ip = re.findall(Pattern,i)
			method=re.findall(Pattern2,i)		
			uri=re.findall(Pattern3,i)
			userAgent=re.findall(Pattern4,i)
			logs.append(ip[0]+" "+method[0]+" "+uri[0]+" "+userAgent[0]+"\n")

		user1=input("Press 1 to PRINT ParserLog or 2 to Save in File >> ")
		if user1=='1':
			for i in logs:
				print("\n",i)
		elif user1=='2':
			print("\n Your Logs saved successfully to 'Parse_output.txt' ")
			F1=open("Parse_output.txt",'w')
			for i in logs:
				F1.write(i)
			F1.close()
		else : 
			print("EROOR !!!! INVALID input")
	except KeyboardInterrupt:
	 		print("ERROR!!!")
	 		sys.exit()
