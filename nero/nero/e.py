import psutil

def get_router_ip():
    # Get the default gateway (router's IP address)
    gateways = psutil.net_if_addrs()
    for interface, addrs in gateways.items():
        for addr in addrs:
            # The default gateway is typically associated with the 'default' route
            if addr.family == psutil.AF_INET and addr.address != "127.0.0.1":
                return addr.address

# Call the function and store the result in a variable
router_ip = get_router_ip()
print(f"Router IP address: {router_ip}")