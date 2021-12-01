
import numpy as np
import defines as defines

def decodeObjectData(data):

    kernelHelper = np.copy(data)
    print("KernelHelper:" + str(kernelHelper))
    posX = np.bitwise_and(defines.MASK_POSX, kernelHelper)
    posX = posX[6:8]
    posXdec = round(float(int.from_bytes(posX, byteorder='little') - 4096)*0.128,0)
    print("Posição x: " + str(posXdec))

    posY = np.bitwise_and(defines.MASK_POSY, kernelHelper)
    posY = posY[4:7]
    posYdec = round(float(int.from_bytes(posY, byteorder='little') - 4096)*0.128,0)
    print("Posição y: " + str(posYdec))

    velX = np.bitwise_and(defines.MASK_VELX, kernelHelper)
    velX = velX[3:5]
    velXdec = round(float(int.from_bytes(velX, byteorder='little') - 1024)*0.1/3.6,0)
    print("Velocidade x: " + str(velXdec))

    velY = np.bitwise_and(defines.MASK_VELY, kernelHelper)
    velY = velY[2:4]
    velYdec = round(float(int.from_bytes(velY, byteorder='little') - 1024)*0.1/3.6,0)
    print("Velocidade y: " + str(velYdec))

    objLen = np.bitwise_and(defines.OBJECT_LEN, kernelHelper)
    objLen = objLen[1:2]
    objLenDec = round(float(int.from_bytes(objLen, byteorder='little')*0.2),0)
    print("Comprimento do objeto: " + str(objLenDec))

    objId = np.bitwise_and(defines.OBJECT_ID, kernelHelper)
    objId = objId[0:1]
    objIdDec = int.from_bytes(objId, byteorder='little')
    print("Id do objeto: " + str(objIdDec))

    return [objIdDec, objLenDec, posXdec, posYdec, velXdec, velYdec]

def bitwiseAnd(mask, data):
    andHelper = np.copy(data)
    anded = np.copy(data)
    for index in range(len(anded)):
        anded[index] = mask[index] & andHelper[index]
    return anded