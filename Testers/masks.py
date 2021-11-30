
import numpy as np
import defines

MASK_POSX = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3F, 0xFE])
MASK_POSY = bytearray([0x00, 0x00, 0x00, 0x00, 0x07, 0xFF, 0xC0, 0x00])
MASK_VELX = bytearray([0x00, 0x00, 0x00, 0x3F, 0xF8, 0x00, 0x00, 0x00])
MASK_VELY = bytearray([0x00, 0x01, 0xFF, 0xC0, 0x00, 0x00, 0x00, 0x00])
OBJECT_LEN = bytearray([0x00, 0xFE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
OBJECT_ID = bytearray([0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

def main():
    print("Main says: Aloha, everybody!")

    #data = bytearray([0x05, 0x02, 0x08, 0x84, 0x29, 0x00, 0xAC, 0x1B, 0x00, 0x2F, 0x06])
    data = bytearray([0x84, 0x29, 0x00, 0xAC, 0x1B, 0x00, 0x2F, 0x06])

    posX = np.bitwise_and(MASK_POSX, data)
    print(posX)

    anded = defines.oldPythonAnd(MASK_POSX, data)
    print(anded)

    posX = posX[6:8]
    posXdec = float(int.from_bytes(posX, byteorder='little'))*0.128
    print(posXdec)

    posY = MASK_POSY and data
    posY = posY[4:7]
    posYdec = float(int.from_bytes(posY, byteorder='little'))*0.128
    print(posYdec)

    velX = MASK_VELX and data
    velX = velX[3:5]
    velXdec = float(int.from_bytes(velX, byteorder='little'))*0.1
    print(velXdec)

    velY = MASK_VELY and data
    velY = velY[1:4]
    velYdec = float(int.from_bytes(velY, byteorder='little'))*0.1
    print(velYdec)

    objLen = OBJECT_LEN and data
    objLen = objLen[1:2]
    objLenDec = float(int.from_bytes(objLen, byteorder='little')*0.2)
    print(objLenDec)

    objId = OBJECT_ID and data
    objId = objId[0:1]
    objIdDec = int.from_bytes(objId, byteorder='little')
    print(objIdDec)

if __name__ == '__main__':
    main()