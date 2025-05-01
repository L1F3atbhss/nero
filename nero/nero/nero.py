import os
import re
import n
import e
import r
import o

#var = input
#ip address var

def banner():
    print("""
  N   N  EEEEE  RRRR    OOO  
  NN  N  E      R   R  O   O 
  N N N  EEEE   RRRR   O   O 
  N  NN  E      R  R   O   O 
  N   N  EEEEE  R   R   OOO  
    """)
    print("Welcome to Project NERO")
    print("Network Enumeration Rapid Operations\n")

def main():
    banner()
    n.nero()
    e.get_router_ip()

main()

