import requests
import os
from colorama import init, Fore, Style

# colorama
init(autoreset=True)

# clear the terminal
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# clear the screen
clear_screen()

# ASCII Art Title with Multi-Tool Name
print(Fore.CYAN + Style.BRIGHT + """
Multi-Tool
""")

# Api ipinfo
token = "8150bb42eda929"

def get_public_ip() -> str:
    """Fecth the public IP address of the user."""
    response = requests.get("https://ipinfo.io/ip")
    return response.text.strip() if response.status_code == 200 else "Unknown"

def get_ip_info(ip_address: str, token: str) -> dict:
    """Fetch IP information using ipinfo.io API."""
    url = f"https://ipinfo.io/{ip_address}?token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(Fore.RED + "Error:", response.status_code)
        return {}
    
def domain_to_ip(domain: str) -> str:
    """Resolve domain name to IP address."""
    url = f"https://dns.google/resolve?name={domain}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for answer in data.get("Answer", []):
            if answer["type"] == 1: # Type 1 means it's an 'A' record (IPv4 address)
                return answer["data"]
        print(Fore.RED + "Error: No 'A' record found for this domain.")
    else:
        print(Fore.REDpi + "Error:", response.status_code)
    return None

def display_menu():
    """Display the main menu for the multi-tool. """
    print(Fore.YELLOW + "=" * 50)
    print(Fore.GREEN + "[1] Geo IP")
    print(Fore.GREEN + "[2] Domain Lookup")
    print(Fore.GREEN + "[0] Exit")
    print(Fore.YELLOW + "=" * 50)

def main():
    while True:
        display_menu()
        choice = input(Fore.GREEN + "Select an option: ").strip()

        if choice == "1":
            ip_address = input(Fore.GREEN + "Enter the IP address you want to look up: ").strip()
            ip_info = get_ip_info(ip_address, token)
            if ip_info:
                print(Fore.YELLOW + "IP Information:")
                for key, value in ip_info.items():
                    print(Fore.GREEN + f"{key.capitalize()}: {Fore.WHITE + str(value)}")
            else:
                print(Fore.RED + "No information available.")

        elif choice == "2":
            domain = input(Fore.GREEN + "Enter the domain name you want to look up: ").strip()
            ip_address = domain_to_ip(domain)
            if ip_address:
                print(Fore.CYAN + f"\nResolve IP address for {domain}: {ip_address}")
            else:
                print(Fore.RED + "Unable to resolve the domain to an IP address.")


        elif choice == "0":
            print(Fore.GREEN + "Exiting Multi-Tool. Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid option. Please try again.")

if __name__ == "__main__":
    main()