import os
import nmap

def get_ipa():
    result = os.popen("ip route show default").read()
    gateway = result.split()[2]
    return gateway

#print(get_default_gateway())

NM = nmap.PortScaner()