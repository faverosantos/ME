# A code by Fávero Santos @ Curitiba, Paraná, Brazil in 25/11/2021

from udp import udpServer

def main():
    print("Aloha!")
    myUDPServer = udpServer()
    myUDPServer.connect()

    while True:
        print("Data from UDP:" + str(myUDPServer.getData()))


if __name__ == '__main__':
    main()

