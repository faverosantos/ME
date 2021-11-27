from udpserver import udpServer
import defines as defines
import multiprocessing
import time

if defines.DEBUG_MODE is True:
    from udpclient import udpClient


def udpWorker(name: str) -> None:
    myUdpClient = udpClient()

    while True:
        myUdpClient.sendData()
        time.sleep(1)

class Processor:

    myUDPServer = 0

    def __init__(self):
        print("Processor says: I am alive!")

        self.myUDPServer = udpServer()
        self.myUDPServer.connect()

        if defines.DEBUG_MODE is True:
            processesList = list()
            udpClientProcess = multiprocessing.Process(target=udpWorker, args=("udpClient",))
            processesList.append(udpClientProcess)
            udpClientProcess.start()

    def listen(self):
        receivedData = self.myUDPServer.getData()
        #print("Data from UDP: " + str(receivedData))
        if receivedData[0:4] == bytearray([0xCA, 0xCB, 0xCC, 0xCD]):
            receivedDataLen = len(receivedData)
            payload = receivedData[receivedDataLen-7:receivedDataLen-4]
            print(f"Received payload is: {payload}")

        # Para ler os hex posicionalmente, é possível usar hex(receivedData[index])
