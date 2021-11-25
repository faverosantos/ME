# A simple UDP server

import socket

class udpServer:

    UDP_PORT_NO = 6664
    #UDP_IP_ADDR = "192.168.11.101"
    UDP_IP_ADDR = "127.0.0.1"
    SV_SOCKET = 0

    def __init__(self):
        pass

    def connect(self):
        self.SV_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.SV_SOCKET.bind((self.UDP_IP_ADDR, self.UDP_PORT_NO))

    def getData(self):
        data, addr = self.SV_SOCKET.recvfrom(1024)
        return data
