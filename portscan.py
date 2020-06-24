from scapy.all import *
import sys
#Suprime mensajes
conf.verb = 0

if len(sys.argv) < 3:
    print(f"python3 {sys.argv[0]} <IP> <PORT>")
    exit(1)
else:
    dst_ip = sys.argv[1]
    dst_port = int(sys.argv[2])

src_port = RandShort()
resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags=0x02),timeout=1)

try:
    if(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags == 0x12):
            send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags=0x14),timeout=1)
            print("Puerto Abierto")
        elif (resp.getlayer(TCP).flags == 0x14):
            print("Puerto Cerrado")
except AttributeError as e:
    print("Sin respuesta")
