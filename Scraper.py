import re
import sys
import subprocess
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
#from urlextract import URLExtract
import socket
import contextlib

def UserInput():
	userInput=input("Enter URL >>  ")
	if re.match(r'(http://|https://).*\.[a-z]{1,3}',userInput):
		return userInput
	else:
 		print("\n ERROR!! InValid HTTP link  \n")
 		sys.exit()

				         # TAGS Function #
def tagsF(soup):
	tags=[]
	for tag in soup.find_all(True):
		tags.append("<"+tag.name+">")
	tagP=set(tags)
	for i in tagP:
 		print (i)

              # Comments Function #

def commentsF(soup):
	for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
		print("<!-- "+comments+" -->")


                #DOMAINS#

def domainsF(sSoup):
	domainList=[]
	pattern=re.findall(r'(www\.)(.+?\.[a-z]{2,3})',sSoup)
	for domain in pattern:
		domainList.append(domain[1])
		final_Dom=set(domainList)
	for i in final_Dom:
		print (i)
	return final_Dom	

               #SubDomain#

def subdomainF(sSoup ,newDomains ):
	res2=[]
	for dom in newDomains:
		pattern=re.compile('[a-z0-9]*\.'+dom)
		resp=re.findall(pattern,sSoup)
		res2.append(list(set(resp)))
	for i in res2:
		print(i)	

def uRL(sSoup):
	result = re.findall(r"\w+://\w+\.\w+\.\w+/?[\w\.\?=#]*", sSoup)
	f_Res=set(result)
	for p in f_Res:
		print("\n",p)



def main():

	try:
		print("For Example >>> https://YourSite.* \n")
		userInput2=UserInput()
		r=requests.get(userInput2) #to get source 
		#print (r.status_code)
		#print (r.url)
		#print (r.headers)
		data = r.text
		# print (data)
		f=open("IndexHtml.txt","w")
		f.write(data)
		f.close()
		html = open("IndexHtml.txt").read()
		soup = BeautifulSoup(html,'lxml')
		sSoup=str(soup)

		press = input("Press '1' to print on Screen or '2' save to scraper.txt file>>  ")
		if press =='1':
			print (" \n \t \t \t \t \t ####### Unique TAGS ####### \n ")
			tagsF(soup)
			print (" \n \t \t \t \t \t ####### Unique COMMENTS ####### \n ")
			commentsF(soup)
			print (" \n \t \t \t \t \t ####### Unique DOMAINS ####### \n ")
			newDomains=domainsF(sSoup)
			print (" \n \t \t \t \t \t ####### Unique SUB-DOMAINS ####### \n ")
			subdomainF(sSoup,newDomains)
			print (" \n \t \t \t \t \t ####### Unique URLS ####### \n ")
			uRL(sSoup)
		elif press=='2':
			print("\n Your outPut saved successfully to 'scraper.txt' ")
			f=open('scraper.txt','w')
			with contextlib.redirect_stdout(f):
				print (" \t \t  \t \t \t ####### Unique TAGS ####### \n ")
				tagsF(soup)
				print (" \n \t \t \t \t \t ####### Unique COMMENTS ####### \n ")
				commentsF(soup)
				print (" \n \t \t \t \t \t ####### Unique DOMAINS ####### \n ")
				newDomains=domainsF(sSoup)
				print (" \n \t \t \t \t \t ####### Unique SUB-DOMAINS ####### \n ")
				subdomainF(sSoup,newDomains)
				print (" \n \t \t \t \t \t ####### Unique URLS ####### \n ")
				uRL(sSoup)

			f.close()
		else:
			print(" ERROR!!!!InValid input ")
			sys.exit()	 
	except KeyboardInterrupt:
	 		print("ERROR!!!")
	 		sys.exit()

