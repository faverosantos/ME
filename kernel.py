
import numpy as np
import defines as defines

def decodeObjectData(data):

    kernelHelper = np.copy(data)
    #print("KernelHelper:" + str(kernelHelper))
    posX = np.bitwise_and(defines.MASK_POSX, kernelHelper)
    posX = posX[6:8]
    posXdec = int.from_bytes(posX, byteorder='big') >> 1
    posXdec = round((posXdec - 4096) * 0.128, 0)
    print("Posição x: " + str(posXdec))

    posY = np.bitwise_and(defines.MASK_POSY, kernelHelper)
    posY = posY[4:7]
    posYdec = int.from_bytes(posY, byteorder='big') >> 6
    posYdec = round((posYdec - 4096)*0.128, 0)
    print("Posição y: " + str(posYdec))

    velX = np.bitwise_and(defines.MASK_VELX, kernelHelper)
    velX = velX[3:5]
    velXdec = int.from_bytes(velX, byteorder='big') >> 3
    velXdec = round((velXdec - 1024) * 0.1 / 3.6, 0)
    print("Velocidade x: " + str(velXdec))

    velY = np.bitwise_and(defines.MASK_VELY, kernelHelper)
    velY = velY[1:4]
    velYdec = int.from_bytes(velY, byteorder='big') >> 6
    velYdec = round((velYdec - 1024) * 0.1 / 3.6, 0)
    print("Velocidade y: " + str(velYdec))

    objLen = np.bitwise_and(defines.OBJECT_LEN, kernelHelper)
    objLen = objLen[1:2]
    objLenDec = int.from_bytes(objLen, byteorder='big') >> 1
    objLenDec = round((objLenDec) * 0.2, 0)
    print("Comprimento do objeto: " + str(objLenDec))

    objId = np.bitwise_and(defines.OBJECT_ID, kernelHelper)
    objId = objId[0:1]
    objIdDec = int.from_bytes(objId, byteorder='big')
    print("Id do objeto: " + str(objIdDec))

    return [objIdDec, objLenDec, posXdec, posYdec, velXdec, velYdec]

def bitwiseAnd(mask, data):
    andHelper = np.copy(data)
    anded = np.copy(data)
    for index in range(len(anded)):
        anded[index] = mask[index] & andHelper[index]
    return anded