import socket
import defines as defines
import numpy as np
import time

class udpClient:

    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = 6664

    clientSocket = 0
    #payload = bytearray([0x00, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0])
    payload = bytearray([0x02, 0xFF, 0x08, 0x00, 0xB1, 0x42, 0x22, 0xA5, 0xB0, 0x31, 0x50, 0x05, 0x00, 0x08, 0x01, 0x41, 0x5A, 0x1E, 0x0B, 0x01, 0x00, 0x00, 0x05, 0x01, 0x08, 0x06, 0x3B, 0x6E, 0xFA, 0x53, 0x3A, 0x02, 0x07, 0x05, 0x02, 0x08, 0x15, 0x00, 0x03, 0xF2, 0xE2, 0x18, 0x05, 0x03, 0x05, 0x03, 0x08, 0xA7, 0x2F, 0x00, 0x04, 0x0E, 0x22, 0x10, 0x18, 0x05, 0x04, 0x08, 0x0A, 0x34, 0x2F, 0x00, 0x03, 0xEF, 0x0A, 0x3C, 0x05, 0x05, 0x08, 0xDA, 0x39, 0x02, 0x5D, 0x63, 0xFF, 0xA7, 0xAC, 0x05, 0x06, 0x08, 0x64, 0x39, 0x39, 0x02, 0x5D, 0x73, 0xF9, 0x67, 0x05, 0x07, 0x08, 0xAD, 0x15, 0x00, 0x03, 0xE9, 0x68, 0x28, 0xC3, 0x05, 0x08, 0x08, 0x64, 0x23, 0x03, 0x5C, 0x83, 0xF2, 0x68, 0xD6, 0x07, 0x82, 0x08, 0x00, 0x02, 0xCB, 0x4A, 0x00, 0x04, 0x00, 0x00, 0x07, 0x83, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x83, 0x02, 0x00, 0x01, 0x07, 0x83, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x07, 0x83, 0x02, 0x00, 0x03, 0x07, 0x85, 0x07, 0x00, 0x7E, 0x61, 0x9D, 0xD2, 0xC4, 0x00, 0x07, 0x83, 0x05, 0xFF, 0xFF, 0x00, 0x00, 0x0E])
    objectIdCounter = 0

    messageToBeSent = defines.HEADER + payload + defines.FOOTER

    def __init__(self):
        print("UDP Client says: I am alive!")
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def setMessage(self, message):
        self.messageToBeSent = message

    def sendData(self):
        self.clientSocket.sendto(defines.HEADER, (self.UDP_IP_ADDRESS, self.UDP_PORT_NO))

        #self.payload[0] = self.objectIdCounter

        # len = 18*3 + 1 = 55
        self.payload = bytearray(
            [0x02, 0xFF, 0x08, 0x00, 0xB1, 0x42, 0x22, 0xA5, 0xB0, 0x31, 0x50, 0x05, 0x00, 0x08, 0x01, 0x41, 0x5A, 0x1E,
             0x0B, 0x01, 0x00, 0x00, 0x05, 0x01, 0x08, 0x06, 0x3B, 0x6E, 0xFA, 0x53, 0x3A, 0x02, 0x07, 0x05, 0x02, 0x08,
             0x15, 0x00, 0x03, 0xF2, 0xE2, 0x18, 0x05, 0x03, 0x05, 0x03, 0x08, 0xA7, 0x2F, 0x00, 0x04, 0x0E, 0x22, 0x10,
             0x18])

        self.clientSocket.sendto(self.payload, (self.UDP_IP_ADDRESS, self.UDP_PORT_NO))

        # len = 18*3 + 1 = 55
        self.payload = bytearray(
            [0x05, 0x04, 0x08, 0x0A, 0x34, 0x2F, 0x00, 0x03, 0xEF, 0x0A, 0x3C, 0x05, 0x05, 0x08, 0xDA, 0x39, 0x02, 0x5D,
             0x63, 0xFF, 0xA7, 0xAC, 0x05, 0x06, 0x08, 0x64, 0x39, 0x39, 0x02, 0x5D, 0x73, 0xF9, 0x67, 0x05, 0x07, 0x08,
             0xAD, 0x15, 0x00, 0x03, 0xE9, 0x68, 0x28, 0xC3, 0x05, 0x08, 0x08, 0x64, 0x23, 0x03, 0x5C, 0x83, 0xF2, 0x68,
             0xD6])

        self.clientSocket.sendto(self.payload, (self.UDP_IP_ADDRESS, self.UDP_PORT_NO))

        # len = 18*3 + 3 = 57
        self.payload = bytearray(
            [0x07, 0x82, 0x08, 0x00, 0x02, 0xCB, 0x4A, 0x00, 0x04, 0x00, 0x00, 0x07, 0x83, 0x06, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x07, 0x83, 0x02, 0x00, 0x01, 0x07, 0x83, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x07, 0x83,
             0x02, 0x00, 0x03, 0x07, 0x85, 0x07, 0x00, 0x7E, 0x61, 0x9D, 0xD2, 0xC4, 0x00, 0x07, 0x83, 0x05, 0xFF, 0xFF,
             0x00, 0x00, 0x0E])

        self.clientSocket.sendto(self.payload, (self.UDP_IP_ADDRESS, self.UDP_PORT_NO))

        #if self.objectIdCounter < 9:
        #    self.objectIdCounter = self.objectIdCounter + 1
        #else:
        #    self.objectIdCounter = 0

        self.clientSocket.sendto(defines.FOOTER, (self.UDP_IP_ADDRESS, self.UDP_PORT_NO))