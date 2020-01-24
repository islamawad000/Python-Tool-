from scapy.all import *
import iptc
import socket
import os


def reOpen(port):
    os.system("nc -nvlp " + str(port) + " &")
    os.system("clear")

def getUnknownOpenPorts():
    global myIP
    host = socket.gethostbyname(myIP)
    openPorts = []
    for port in range(1, 30000):
        if port not in wellknown and port < 30000:
            scannerTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            status = scannerTCP.connect_ex((host, port))
            if not status:
                openPorts.append(port) 
    for p in openPorts:
        os.system("nc -nvlp " + str(p) + " &")
        os.system("clear")   
    return openPorts

def blockIP(ip):
    #add rule to iptables-legacy
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    rule = iptc.Rule()
    rule.in_interface = "eth0"
    target = iptc.Target(rule, "DROP")
    rule.target = target
    rule.src = ip  # ip in string format
    chain.insert_rule(rule)

    os.system(f"iptables -A OUTPUT -d {ip} -j DROP") #add a rule to iptables as well

def print_summary(pkt):
    global myIP
    global unKnown
    tcp_sport = ""
    if 'TCP' in pkt:
        tcp_sport=pkt['TCP'].sport

    if (pkt['IP'].src == myIP)  and tcp_sport in unKnown:
        blockIP(pkt['IP'].dst)
        reOpen(tcp_sport)
        print("Attack detected!")
        print(f"Blocking {pkt['IP'].dst} ...\nBlocked!\n")


def Monitor():
    sniff(filter="ip",prn=print_summary)
    sniff(filter="ip and host " + myIP, prn=print_summary)

wellknown = [1, 5, 7, 18, 20, 21, 22, 23, 25, 29, 37, 42, 43, 49, 53,
 69, 70, 79, 80, 103, 108, 109, 110, 115, 118, 119, 137, 139, 143,
 150, 156, 161, 179, 190, 194, 197, 389, 396, 443, 444, 445, 458, 546, 547, 563, 569, 1080]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myIP = s.getsockname()[0]
s.close()
unKnown = getUnknownOpenPorts()


def main():
    if(len(unKnown)):
        print(f"Monitoring {myIP}....")
        Monitor()
    else:
        print("No Open ports were detected\ngo open some first ;)")
