import socket
import defines as defines
import numpy as np
import time

class udpClient:

    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = 6664

    clientSocket = 0
    payload = bytearray([0x00, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0])
    objectIdCounter = 0

    messageToBeSent = defines.HEADER + payload + defines.FOOTER

    def __init__(self):
        print("UDP Client says: I am alive!")
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def setMessage(self, message):
        self.messageToBeSent = message

    def sendData(self):
        self.clientSocket.sendto(defines.HEADER, (self.UDP_IP_ADDRESS, self.UDP_PORT_NO))

        self.payload[0] = self.objectIdCounter
        self.clientSocket.sendto(self.payload, (self.UDP_IP_ADDRESS, self.UDP_PORT_NO))

        if self.objectIdCounter < 9:
            self.objectIdCounter = self.objectIdCounter + 1
        else:
            self.objectIdCounter = 0

        self.clientSocket.sendto(defines.FOOTER, (self.UDP_IP_ADDRESS, self.UDP_PORT_NO))