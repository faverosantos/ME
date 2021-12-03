import numpy as np

from udpserver import udpServer
from vehicle import Vehicle
import kernel as kernel
import defines as defines
from collections import deque
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

        #manager = multiprocessing.Manager()
        #mutex = manager.Lock()

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
                #print("H: " + str(receivedData))
                package = receivedData[4:len(receivedData)]

            elif receivedData[len(receivedData)-4:len(receivedData)] == defines.FOOTER and newMessage is True:
                #print("F: " + str(receivedData))
                newMessage = False

                package = package + receivedData[:len(receivedData)-5]
                # TODO: na verdade é len(receivedData)-4, já que a posição -5 é o CRC do dado, que nesse código não está sendo tratado.
                #print("Listened package: " + str(package) + "with size: " + str(len(package)))
                #print("Listen package len:" + str(len(package)))

                packageQueue.put(package)
                package = bytearray()
                receivedData = 0

            elif newMessage is True:
                # TODO: Deve existir uma verificação de primeira mensagem aqui para que não fique acumulando mensagens indevidas
                #print("B: " + str(receivedData))
                package = package + receivedData

            else:
                package = bytearray()
                receivedData = 0
            #time.sleep(0.1)

    def process(self, name, packageQueue, objectQueue):
        print("Processor 'process' function is working!")
        'This function is responsible for managing objects'

        vehicleList = list()
        for index in range(3*defines.MAX_OBJECTS):
            newVehicle = Vehicle()
            vehicleList.append(newVehicle)
            del newVehicle

        while True:
            #TODO: tratar a exceção caso o packageQueue esteja vazio

            PROCESS = True

            messageToProcess = bytearray()
            messageToProcess = bytearray(packageQueue.get()).copy()
            #print("Processor package len:" + str(len(messageToProcess)))

            #if len(messageToProcess) < 100:
            #    print("Bypassed!")
            #    messageToProcess = 0
            #    PROCESS = False

            #print("Mensagem para ser processada (ANTES): " + str(messageToProcess) + "com comprimento " + str(len(messageToProcess)))
            #print("Comprimento antes: " + str(len(messageToProcess)))
            #retries = 20

            if PROCESS:
                while len(messageToProcess) > 0:# or retries > 0:
                    if messageToProcess[0:2] == defines.OBJECT_CONTROL:
                        print("OBJECT_CONTROL recebido!")

                        if messageToProcess[2:3] == bytearray([0x08]):
                            print("OBJECT_CONTROL processado!")
                            data = messageToProcess[3:11]
                            #objectControlResult = kernel.decodeObjectControlMessage(bytearray(data))
                            messageToProcess = messageToProcess[11:]
                            #print("Depois: " + str(messageToProcess))

                        print("")

                    elif messageToProcess[0:2] == defines.SM_TIME_MESSAGE:
                        print("SM_TIME_MESSAGE recebido!")

                        if messageToProcess[2:3] == bytearray([0x08]):
                            print("SM_TIME_MESSAGE processado!")
                            data = messageToProcess[3:11]
                            #objectControlResult = kernel.decodeTimeMessage(bytearray(data))
                            messageToProcess = messageToProcess[11:]
                            #print("Depois: " + str(messageToProcess))

                        print("")

                    elif messageToProcess[0:2] == defines.SM_0x734:
                        print("SM_0x74 recebido!")
                        #print(messageToProcess)

                        if messageToProcess[2:3] == bytearray([0x08]):
                            print("SM_0x74 processado")
                            data = messageToProcess[3:11]
                            messageToProcess = messageToProcess[11:]
                            #print("Depois: " + str(messageToProcess))

                        print("")

                    elif messageToProcess[0:2] == defines.SM_0x782:
                        print("SM_0x782 recebido!")
                        #print(messageToProcess)

                        if messageToProcess[2:3] == bytearray([0x08]):
                            print("SM_0x782 processado")
                            data = messageToProcess[3:11]
                            #timeResult = kernel.decodeTimeMessage(bytearray(data))
                            messageToProcess = messageToProcess[11:]
                            #print("Depois: " + str(messageToProcess))

                        print("")

                    elif messageToProcess[0:2] == defines.SM_0x783:
                        print("SM_0x783 recebido!")
                        #print(messageToProcess)

                        if messageToProcess[2:3] == bytearray([0x02]):
                            print("wrongDirectionResult processado")
                            data = messageToProcess[3:5]
                            #wrongDirectionResult = kernel.decodeWrongDirectionMessage(bytearray(data))
                            messageToProcess = messageToProcess[5:]
                            #print("Depois: " + str(messageToProcess))

                        elif messageToProcess[2:3] == bytearray([0x03]):
                            print("SM_0x783 len 3 processado")
                            data = messageToProcess[3:6]
                            messageToProcess = messageToProcess[6:]
                            #print("Depois: " + str(messageToProcess))

                        elif messageToProcess[2:3] == bytearray([0x05]):
                            print("relayControlResult processado")
                            data = messageToProcess[3:8]
                            #relayControlResult = kernel.decodeRelayControlMessage(bytearray(data))
                            messageToProcess = messageToProcess[8:]
                            #print("Depois: " + str(messageToProcess))

                        elif messageToProcess[2:3] == bytearray([0x06]):
                            print("presenceResult processado")
                            data = messageToProcess[3:9]
                            #presenceResult = kernel.decodePresenceMessage(bytearray(data))
                            messageToProcess = messageToProcess[9:]
                            #print("Depois: " + str(messageToProcess))

                        print("")

                    elif messageToProcess[0:2] == defines.SM_0x784:
                        print("SM_0x784 recebido!")
                        #print(messageToProcess)

                        if messageToProcess[2:3] == bytearray([0x03]):
                            print("SM_0x784 len 3 processado!")
                            data = messageToProcess[3:6]
                            messageToProcess = messageToProcess[6:]
                            #print("Depois: " + str(messageToProcess))
                            #print("Len mensagem: " + str(len(messageToProcess)))

                        if messageToProcess[2:3] == bytearray([0x04]):
                            print("SM_0x784 len 4 processado!")
                            data = messageToProcess[3:7]
                            messageToProcess = messageToProcess[7:]
                            #print("Depois: " + str(messageToProcess))
                            #print("Len mensagem: " + str(len(messageToProcess)))

                        print("")

                    elif messageToProcess[0:2] == defines.SM_0x785:
                        print("SM_0x785 recebido!")
                        #print(messageToProcess)

                        if messageToProcess[2:3] == bytearray([0x07]):
                            print("SM_0x785 processado!")
                            data = messageToProcess[3:10]
                            messageToProcess = messageToProcess[10:]
                            #print("Depois: " + str(messageToProcess))

                        print("")

                    elif messageToProcess[0:2] == defines.SENSOR_CONTROL:
                        print("SENSOR_CONTROL recebido!")

                        if messageToProcess[2:3] == bytearray([0x08]):
                            print("SENSOR_CONTROL processado!")
                            data = messageToProcess[3:11]
                            #sensorControlResult = kernel.decodeSensorControlMessage(bytearray(data))
                            messageToProcess = messageToProcess[11:]
                            #print("Depois: " + str(messageToProcess))

                        print("")

                    elif int.from_bytes(messageToProcess[0:2], byteorder='big') >= int.from_bytes(bytearray([0x05, 0x02]), byteorder='big') and int.from_bytes(messageToProcess[0:2], byteorder='big') <= int.from_bytes(bytearray([0x05, 0x7F]), byteorder='big'):
                        print("OBJECT_DATA recebido!")

                        if messageToProcess[2:3] == bytearray([0x08]):
                            print("OBJECT_DATA processado!")

                            data = messageToProcess[3:11]
                            objectDataResult = kernel.decodeObjectData(bytearray(data))
                            messageToProcess = messageToProcess[11:]
                            #print("Depois: " + str(messageToProcess))

                            #if len(vehicleList[id].getPosition()) == 0:
                            #    vehicleList[id].setId(id)
                            ##    vehicleList[id].setLen(com)
                             #   vehicleList[id].setPosition(posX, posY)
                            #    vehicleList[id].setVelocity(velX, velY)
                            #else:
                            #    vehicleList[id].setPosition(posX, posY)
                            #    vehicleList[id].setVelocity(velX, velY)

                        print("")

                    elif messageToProcess[0:2] == defines.SYNC_MESSAGE:
                        print("SYNC_MESSAGE recebido!")

                        if messageToProcess[2:3] == bytearray([0x08]):
                            print("SYNC_MESSAGE processado!")
                            data = messageToProcess[3:11]
                            #syncResult = kernel.decodeSyncMessage(bytearray(data))
                            messageToProcess = messageToProcess[11:]
                            #print("Depois: " + str(messageToProcess))

                        print("")

                    else:
                        print("Resto: " + str(messageToProcess))
                        messageToProcess = bytearray()

                #time.sleep(2)
#                #retries = retries - 1

            #self.packageList.pop(0)




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

