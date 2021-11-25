# A code by Fávero Santos @ Curitiba, Paraná, Brazil in 25/11/2021

import socket
import time

def main():
    print("Aloha!")
    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = 6664
    Message = str.encode("Hello, Server")
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        time.sleep(1)
        clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))


if __name__ == '__main__':
    main()


