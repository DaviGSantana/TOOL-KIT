import os
import platform
from queue import Queue 
import threading, socket, sys

def clear_terminal():
    system = platform.system()
    if(system == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def subdomain_hunter():
    print("Modo de uso: target -w /caminho/wordlist")
    

def print_banner():
    banner = """
    
██████╗ ███████╗███╗   ██╗████████╗███████╗███████╗████████╗████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗██╗████████╗
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║ ██╔╝██║╚══██╔══╝
██████╔╝█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗   ██║█████╗██║   ██║   ██║██║   ██║██║     █████╔╝ ██║   ██║   
██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║   ██║╚════╝██║   ██║   ██║██║   ██║██║     ██╔═██╗ ██║   ██║   
██║     ███████╗██║ ╚████║   ██║   ███████╗███████║   ██║      ██║   ╚██████╔╝╚██████╔╝███████╗██║  ██╗██║   ██║   
╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
                                        Autor: DaviGSantana
    """
    print(banner)

if __name__ == "__main__":
    print_banner()
    while True:
        print("[INFO] Main Menu")
        print("1. Information Gathering")
        print("2. Vulnerability Scanning")
        print("3. Manual Testing")
        print("4. Exploitation")
        print("5. Post-Exploitation")
        print("6. Reporting")
        print("7. Exit")
        number = input("Enter your choice: ")
        if number.isdigit():
            number = int(number)
            if (number == 1):
                clear_terminal()
                subdomain_hunter()
                target = input("Digite o target: ")
