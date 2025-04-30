import os
#import nmap

def banner():
    print("""
  N   N  EEEEE  RRRR    OOO  
  NN  N  E      R   R  O   O 
  N N N  EEEE   RRRR   O   O 
  N  NN  E      R  R   O   O 
  N   N  EEEEE  R   R   OOO  

Network Enumeration Rapid Operations
    """)
    print("Welcome to Project NERO")
    print("Network Enumeration Rapid Operations\n")

def menu():
    print("Choose a tool:")
    print("[N] Nmap - Network Scanner")
    print("[E] Enum4linux - Enumerate Shares/Users")
    print("[R] Rustscan - Fast Port Scanner")
    print("[O] OpenVAS - Vulnerability Scanner")
    print("[Q] Quit")

def run_nmap():
    target = input("Enter target IP or domain: ")
    os.system(f"nmap -sV -Pn {target}")

def run_enum4linux():
    target = input("Enter target IP: ")
    os.system(f"enum4linux -a {target}")

def run_rustscan():
    target = input("Enter target IP: ")
    os.system(f"rustscan -a {target} -- -sV")

def run_openvas():
    print("OpenVAS usually runs as a web server (GVM).")
    print("Launching OpenVAS (GVM)...")
    os.system("gvm-start")  # adjust depending on your setup

def main():
    banner()
    while True:
        menu()
        choice = input("\nSelect: ").lower()
        if choice == 'n':
            run_nmap()
        elif choice == 'e':
            run_enum4linux()
        elif choice == 'r':
            run_rustscan()
        elif choice == 'o':
            run_openvas()
        elif choice == 'q':
            print("Exiting Nero. Stay sharp.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
