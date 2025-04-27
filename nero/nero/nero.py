import os
import nmap
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
print(router_ip)

NM = nmap.PortScaner()