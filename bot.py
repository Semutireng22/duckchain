import requests
import time
import signal
import sys
from colorama import Fore, Style, init

# Inisialisasi Colorama
init(autoreset=True)

# Fungsi untuk membaca kode otentikasi dari file
def read_auth_token(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Fungsi untuk mendapatkan data pengguna
def get_user_info(auth_token):
    url = "https://preapi.duckchain.io/user/info"
    headers = {
        'Authorization': f'tma {auth_token}',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
    }
    
    response = requests.get(url, headers=headers)
    return response

# Fungsi untuk mengeksekusi API quack
def execute_quack(auth_token):
    url = "https://preapi.duckchain.io/quack/execute"
    headers = {
        'Authorization': f'tma {auth_token}',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129", "Microsoft Edge WebView2";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
    }
    
    response = requests.get(url, headers=headers)
    return response

# Fungsi untuk menangani keluar aman
def signal_handler(sig, frame):
    print(Fore.YELLOW + "\nProgram dihentikan dengan aman. Airdrop ASC!!!")
    sys.exit(0)

# Menangani sinyal CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Banner ASCII
banner = r"""
 █████╗ ██╗██████╗ ██████╗ ██████╗  ██████╗ ██████╗      █████╗ ███████╗ ██████╗
██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╔══██╗██╔════╝██╔════╝
███████║██║██████╔╝██║  ██║██████╔╝██║   ██║██████╔╝    ███████║███████╗██║     
██╔══██║██║██╔══██╗██║  ██║██╔══██╗██║   ██║██╔═══╝     ██╔══██║╚════██║██║     
██║  ██║██║██║  ██║██████╔╝██║  ██║╚██████╔╝██║         ██║  ██║███████║╚██████╗
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝         ╚═╝  ╚═╝╚══════╝ ╚═════╝
                                                                                
====================================================
     BOT                : DuckChain Quack
     Telegram Channel   : @airdropasc
     Telegram Group     : @autosultan_group
====================================================
"""

# Menampilkan banner
print(Fore.CYAN + banner)

# Loop utama program
username_displayed = False  # Flag untuk menampilkan username dan total duck hanya sekali

# Loop utama program
while True:
    # Membaca kode otentikasi dari token.txt
    auth_token = read_auth_token('token.txt')

    # Mendapatkan data pengguna
    user_response = get_user_info(auth_token)

    # Memeriksa status kode respons untuk data pengguna
    if user_response.status_code == 200:
        user_data = user_response.json()
        default_name = user_data['data']['defaultName']
        total_duck = user_data['data']['decibels']

        # Menampilkan Username dan Total Duck hanya sekali
        if not username_displayed:
            print(Fore.YELLOW + f"Username: {default_name}")
            print(Fore.YELLOW + f"Total Duck: {total_duck} DUCK")
            print(Fore.CYAN + f"-----------------------------")
            username_displayed = True  # Set flag ke True setelah ditampilkan

        # Menjalankan API quack
        quack_response = execute_quack(auth_token)

        # Memeriksa status kode respons untuk API quack
        if quack_response.status_code == 200:
            quack_data = quack_response.json()
            total_quack = quack_data['data']['quackTimes']  # Mengambil total quack
            current_total_duck = quack_data['data']['decibel']  # Ambil total duck terbaru
            print(Fore.GREEN + f"[ASC] Quack executed successfully. Total Quack: {total_quack} | Total Duck: {current_total_duck} DUCK")
        else:
            print(Fore.RED + f"[ASC] ERROR: {quack_response.status_code} - {quack_response.text}")
    else:
        print(Fore.RED + f"[ASC] ERROR: {user_response.status_code} - {user_response.text}")

    # Menunggu sebelum eksekusi berikutnya
    time.sleep(2)
