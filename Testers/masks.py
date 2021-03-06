
import numpy as np
import defines
import kernel as kernel
import vehicle as Object
import collections

MASK_POSX = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3F, 0xFE])
MASK_POSY = bytearray([0x00, 0x00, 0x00, 0x00, 0x07, 0xFF, 0xC0, 0x00])
MASK_VELX = bytearray([0x00, 0x00, 0x00, 0x3F, 0xF8, 0x00, 0x00, 0x00])
MASK_VELY = bytearray([0x00, 0x01, 0xFF, 0xC0, 0x00, 0x00, 0x00, 0x00])
OBJECT_LEN = bytearray([0x00, 0xFE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
OBJECT_ID = bytearray([0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

def main():
    print("Main says: Aloha, everybody!")

    teste = bytearray([0xCA, 0xFE, 0xBA, 0xBE])
    print(int.from_bytes(teste, byteorder='big'))
    teste.reverse()
    print(teste)
    print(int.from_bytes(teste, byteorder='little'))


    teste = 0x03
    a = teste >> 1

    #data = bytearray([0x05, 0x02, 0x08, 0x84, 0x29, 0x00, 0xAC, 0x1B, 0x00, 0x2F, 0x06])
    data = bytearray([0xa2, 0x5c, 0x00, 0x20, 0x04, 0x0f, 0xa1, 0xf8])



    a = kernel.decodeObjectControlMessage(data)

    pass



if __name__ == '__main__':
    main()