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
    package = bytearray()
    newMessage = False
    processesList = list()
    packageReady = False

    def __init__(self):
        print("Processor says: I am alive!")

        self.myUDPServer = udpServer()
        self.myUDPServer.connect()

        if defines.DEBUG_MODE is True:

            udpClientProcess = multiprocessing.Process(target=udpWorker, args=("udpClient",))
            self.processesList.append(udpClientProcess)
            udpClientProcess.start()

        udpServerListener = multiprocessing.Process(target=self.listen, args=("udpServerListener",))
        self.processesList.append(udpServerListener)
        udpServerListener.start()

        udpServerProcessor = multiprocessing.Process(target=self.process, args=("udpServerProcessor",))
        self.processesList.append(udpServerProcessor)
        udpServerProcessor.start()

    def listen(self, name: str) -> None:
        'This is the multi-process version of the listen function. It listens and create a package from the messages received by UDP'
        while True:
            receivedData = self.myUDPServer.getData()
            if receivedData[0:4] == defines.HEADER and self.newMessage is False:
                self.newMessage = True

            elif receivedData[len(receivedData)-4:len(receivedData)] == defines.FOOTER and self.newMessage is True:
                self.newMessage = False
                self.package.clear()
            else:
                self.package = self.package + receivedData
                print("Mesangem recebida é:" + str(self.package))
                self.packageReady = True
            time.sleep(0.1)

    def process(self, name: str) -> None:
        print("Processor 'process' function is working!")
        'This function is responsible for processing the data made available at listen function'
        while True:
            self.packageReady = False #TODO: implementar como mutex a flag packageRDY
            time.sleep(0.1)

    #def listen(self):
    #    'This is the original version of the listen function. It listens and create a package from the messages received by UDP'
    #    receivedData = self.myUDPServer.getData()
    #    if receivedData[0:4] == defines.header and self.newMessage is False:
    #        self.newMessage = True
    #
    #    elif receivedData[len(receivedData)-4:len(receivedData)] == defines.footer and self.newMessage is True:
    #        self.newMessage = False
    #        self.package.clear()
    #    else:
    #        self.package = self.package + receivedData
    #        print("Mesangem recebida é:" + str(self.package))

