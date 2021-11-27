import socket

class udpClient:

    clientSocket = 0
    header = 'CACBCCCD'
    footer = 'CACBCCCD'
    payload = 'FAA3A0'

    messageToBeSent = bytes.fromhex(header + payload + footer)
    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = 6664

    def __init__(self):
        print("UDP Client says: I am alive!")
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def setMessage(self, message):
        self.messageToBeSent = message

    def sendData(self):
        self.clientSocket.sendto(self.messageToBeSent, (self.UDP_IP_ADDRESS, self.UDP_PORT_NO))