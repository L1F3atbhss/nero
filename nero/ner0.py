import os
#import nmap
import platform
import re

def get_router_ip():
    system = platform.system()
    if system == "Windows":
        output = os.popen("ipconfig").read()
        match = re.search(r"Default Gateway.+?: (\d+\.\d+\.\d+\.\d+)", output)
        return match.group(1) if match else None
    else:
        output = os.popen("ip route show default").read()
        parts = output.split()
        return parts[2] if "default" in parts else None

router_ip = get_router_ip()
print(f"Router IP: {router_ip}")

nm = nmap.PortScanner()

# Scan the router
nm.scan(router_ip, arguments='-sV -Pn -T4')  # -sV = detect service version

# Print open ports with service info
for proto in nm[router_ip].all_protocols():
    ports = nm[router_ip][proto].keys()
    for port in ports:
        service = nm[router_ip][proto][port]['name']
        state = nm[router_ip][proto][port]['state']
        print(f"Port {port}/{proto} is {state}, service: {service}")
