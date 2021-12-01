import numpy as np

from udpserver import udpServer
from object import Object
import kernel as kernel
import defines as defines
import multiprocessing
from multiprocessing import Queue


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
    #package = bytearray()

    processesList = list()

    packageReady = False

    packageQueue = Queue()
    'packageQueue é a fila de pacotes divida entre os processos'

    objectQueue = Queue()
    'objectQueue é a fila de objetos divida entre os processos'


    def __init__(self):
        print("Processor says: I am alive!")

        self.myUDPServer = udpServer()
        self.myUDPServer.connect()

        if defines.DEBUG_MODE is True:
            udpClientProcess = multiprocessing.Process(target=udpWorker, args=("udpClient",))
            self.processesList.append(udpClientProcess)
            udpClientProcess.start()

        udpServerListener = multiprocessing.Process(target=self.listen, args=("udpServerListener", self.packageQueue))
        self.processesList.append(udpServerListener)
        udpServerListener.start()

        udpServerProcessor = multiprocessing.Process(target=self.process, args=("udpServerProcessor", self.packageQueue, self.objectQueue))
        self.processesList.append(udpServerProcessor)
        udpServerProcessor.start()

    def listen(self, name, packageQueue):
        'This is the multi-process version of the listen function. It listens and create a package from the messages received by UDP'

        newMessage = False
        package = bytearray()

        while True:
            receivedData = self.myUDPServer.getData()
            if receivedData[0:4] == defines.HEADER and newMessage is False:
                newMessage = True
                package = receivedData[4:len(receivedData)]

            elif receivedData[len(receivedData)-4:len(receivedData)] == defines.FOOTER and newMessage is True:
                newMessage = False

                packageQueue.put(package)
                package = bytearray()

            elif newMessage is True:
                # TODO: Deve existir uma verificação de primeira mensagem aqui para que não fique acumulando mensagens indevidas
                package = package + receivedData
            else:
                pass
            time.sleep(0.1)

    def process(self, name, packageQueue, objectQueue):
        print("Processor 'process' function is working!")
        'This function is responsible for managing objects'

        objectList = [Object]*127

        while True:
            #TODO: tratar a exceção caso o packageQueue esteja vazio
            messageToProcess = packageQueue.get()


            print("Mensagem para ser processada (ANTES): " + str(messageToProcess) + "com comprimento " + str(len(messageToProcess)))
            #print("Comprimento antes: " + str(len(messageToProcess)))
            retries = 10
            while retries > 0:
                intMessageToProcess = int.from_bytes(messageToProcess[0:2], byteorder='little')
                if messageToProcess[0:2] == defines.OBJECT_CONTROL:
                    print("OBJECT_CONTROL recebido!")
                    messageToProcess = messageToProcess[11:]
                    # Faz o que tem que fazer, remove da lista

                elif messageToProcess[0:2] == defines.SENSOR_CONTROL:
                    print("SENSOR_CONTROL recebido!")
                    messageToProcess = messageToProcess[11:]
                    # Faz o que tem que fazer, remove da lista

                elif intMessageToProcess <= defines.INT_LAST_OBJECT_DATA and intMessageToProcess >= defines.INT_FIRST_OBJECT_DATA:
                    print("OBJECT_DATA recebido!")

                    if defines.DEBUG_MODE:
                        data = messageToProcess
                    else:
                        data = messageToProcess[3:11]

                    # Faz o que tem que fazer, remove da lista
                    if len(data) == 8:
                        objectData = kernel.decodeObjectData(bytearray(data))
                        objectList[objectData[0]].setId(objectData[0]) # A própria posição na lista é o id do objeto ;)
                        objectList[objectData[0]].setLen(objectData[1])
                        objectList[objectData[0]].setPosition(objectData[2], objectData[3])
                        objectList[objectData[0]].setVelocity(objectData[4], objectData[5])

                    messageToProcess = messageToProcess[11:]


                elif messageToProcess[0:2] == defines.SYNC_MESSAGE:
                    print("SYNC_MESSAGE recebido!")
                    messageToProcess = messageToProcess[11:]
                    # Faz o que tem que fazer, remove da lista

                #print("Mensagem para ser processada (DEPOIS): " + str(messageToProcess) + "com comprimento " + str(len(messageToProcess)))
                retries = retries - 1

            #self.packageList.pop(0)

            #time.sleep(0.1)


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

