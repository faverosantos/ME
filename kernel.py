
import numpy as np
import defines as defines

def decodeWrongDirectionMessage(data):

    kernelHelper = np.copy(data)
    # print("KernelHelper:" + str(kernelHelper))
    featureId = bitwiseAnd(defines.MASK_SM_FEATURE_ID, kernelHelper)
    featureId = featureId[1:2]
    featureIdDec = int.from_bytes(featureId, byteorder='big')
    print("featureIdDec: " + str(featureIdDec))

    measurementLine = bitwiseAnd(defines.MASK_SM_MEASUREMENT_LINE, kernelHelper)
    measurementLine = measurementLine[1:2]
    measurementLineDec = int.from_bytes(measurementLine, byteorder='big') >> 1
    print("measurementLineDec: " + str(measurementLineDec))

    whichLane = bitwiseAnd(defines.MASK_SM_WHICH_LANE, kernelHelper)
    whichLane = whichLane[0:1]
    whichLaneDec = int.from_bytes(whichLane, byteorder='big')
    print("whichLaneDec: " + str(whichLaneDec))

    return [featureIdDec, measurementLineDec, whichLaneDec]

def decodeRelayControlMessage(data):

    kernelHelper = np.copy(data)
    # print("KernelHelper:" + str(kernelHelper))
    relayMessageId = bitwiseAnd(defines.MASK_SM_RELAY_MESSAGE_ID, kernelHelper)
    relayMessageId = relayMessageId[4:5]
    relayMessageIdDec = int.from_bytes(relayMessageId, byteorder='big')
    print("relayMessageIdDec: " + str(relayMessageIdDec))

    relay0to7status = bitwiseAnd(defines.MASK_SM_RELAY_0_TO_7_STATUS, kernelHelper)
    relay0to7status = relay0to7status[3:4]
    relay0to7statusDec = int.from_bytes(relay0to7status, byteorder='big') >> 1
    print("relay0to7statusDec: " + str(relay0to7statusDec))

    relay8to15status = bitwiseAnd(defines.MASK_SM_RELAY_8_TO_15_STATUS, kernelHelper)
    relay8to15status = relay8to15status[2:3]
    relay8to15statusDec = int.from_bytes(relay8to15status, byteorder='big')
    print("relay8to15statusDec: " + str(relay8to15statusDec))

    relay0to7assignment = bitwiseAnd(defines.MASK_SM_RELAY_0_TO_7_ASSIGNMENT, kernelHelper)
    relay0to7assignment = relay0to7assignment[1:2]
    relay0to7assignmentDec = int.from_bytes(relay0to7assignment, byteorder='big')
    print("relay0to7assignmentDec: " + str(relay0to7assignmentDec))

    relay8to15assignment = bitwiseAnd(defines.MASK_SM_RELAY_8_TO_15_ASSIGNMENT, kernelHelper)
    relay8to15assignment = relay8to15assignment[0:1]
    relay8to15assignmentDec = int.from_bytes(relay8to15assignment, byteorder='big')
    print("relay8to15assignmentDec: " + str(relay8to15assignmentDec))

    return [relayMessageIdDec, relay0to7statusDec, relay8to15statusDec, relay0to7assignmentDec, relay8to15assignmentDec]

def decodePresenceMessage(data):

    kernelHelper = np.copy(data)
    #print("KernelHelper:" + str(kernelHelper))
    featurePartId = bitwiseAnd(defines.MASK_SM_FEATURE_PART_ID, kernelHelper)
    featurePartId = featurePartId[5:6]
    featurePartIdDec = int.from_bytes(featurePartId, byteorder='big')
    print("featurePartIdDec: " + str(featurePartIdDec))

    measurementLine = bitwiseAnd(defines.MASK_SM_MEASUREMENT_LINE, kernelHelper)
    measurementLine = measurementLine[5:6]
    measurementLineDec = int.from_bytes(measurementLine, byteorder='big') >> 1
    print("measurementLineDec: " + str(measurementLineDec))

    class0 = bitwiseAnd(defines.MASK_SM_CLASS0, kernelHelper)
    class0 = class0[4:5]
    class0Dec = int.from_bytes(class0, byteorder='big')
    print("class0Dec: " + str(class0Dec))

    class1 = bitwiseAnd(defines.MASK_SM_CLASS1, kernelHelper)
    class1 = class1[3:4]
    class1Dec = int.from_bytes(class1, byteorder='big')
    print("class1Dec: " + str(class1Dec))

    class2 = bitwiseAnd(defines.MASK_SM_CLASS2, kernelHelper)
    class2 = class2[2:3]
    class2Dec = int.from_bytes(class2, byteorder='big')
    print("class2Dec: " + str(class2Dec))

    class3 = bitwiseAnd(defines.MASK_SM_CLASS3, kernelHelper)
    class3 = class3[1:2]
    class3Dec = int.from_bytes(class3, byteorder='big')
    print("class3Dec: " + str(class3Dec))

    class4 = bitwiseAnd(defines.MASK_SM_CLASS4, kernelHelper)
    class4 = class4[1:2]
    class4Dec = int.from_bytes(class4, byteorder='big')
    print("class4Dec: " + str(class4Dec))

    return [featurePartIdDec, measurementLineDec, class0Dec, class1Dec, class2Dec, class3Dec, class4Dec]

def decodeTimeMessage(data):

    kernelHelper = np.copy(data)
    #print("KernelHelper:" + str(kernelHelper))
    sensorId = bitwiseAnd(defines.MASK_SM_SENSOR_ID, kernelHelper)
    sensorId = sensorId[7:8]
    sensorIdDec = int.from_bytes(sensorId, byteorder='big')
    print("sensorIdDec: " + str(sensorIdDec))

    intervalCountdown = bitwiseAnd(defines.MASK_SM_INTERVAL_COUNTDOWN, kernelHelper)
    intervalCountdown = intervalCountdown[7:8]
    intervalCountdownDec = int.from_bytes(intervalCountdown, byteorder='big') >> 4
    print("intervalCountdownDec: " + str(intervalCountdownDec))

    numberOfLanes = bitwiseAnd(defines.MASK_SM_NUMBER_OF_LANES, kernelHelper)
    numberOfLanes = numberOfLanes[4:6]
    numberOfLanesDec = int.from_bytes(numberOfLanes, byteorder='big')
    print("numberOfLanesDec: " + str(numberOfLanesDec))

    serialNumber = bitwiseAnd(defines.MASK_SM_SERIAL_NUMBER, kernelHelper)
    serialNumber = serialNumber[0:4]
    serialNumberDec = int.from_bytes(serialNumber, byteorder='big')
    print("serialNumberDec: " + str(serialNumberDec))

    return [sensorIdDec, intervalCountdown, numberOfLanesDec, serialNumberDec]

def decodeSyncMessage(data):

    kernelHelper = np.copy(data)
    #print("KernelHelper:" + str(kernelHelper))
    counter = bitwiseAnd(defines.MASK_COUNTER, kernelHelper)
    counter = counter[2:6]
    counterDec = int.from_bytes(counter, byteorder='big')
    counterDec = counterDec * 0.8
    print("sensorStatusDec (us): " + str(counterDec))

    return counterDec

def decodeSensorControlMessage(data):

    kernelHelper = np.copy(data)
    #print("KernelHelper:" + str(kernelHelper))
    sensorStatus = bitwiseAnd(defines.MASK_SENSOR_STATUS, kernelHelper)
    sensorStatus = sensorStatus[7:8]
    sensorStatusDec = int.from_bytes(sensorStatus, byteorder='big')
    print("sensorStatusDec: " + str(sensorStatusDec))

    interfaceMode = bitwiseAnd(defines.MASK_INTERFACE_MODE, kernelHelper)
    interfaceMode = interfaceMode[6:7]
    interfaceModeDec = int.from_bytes(interfaceMode, byteorder='big')
    print("interfaceModeDec: " + str(interfaceModeDec))

    networkId = bitwiseAnd(defines.MASK_NETWORK_ID, kernelHelper)
    networkId = networkId[6:7]
    networkIdDec = int.from_bytes(networkId, byteorder='big') >> 4
    print("networkIdDec: " + str(networkIdDec))

    diagnose = bitwiseAnd(defines.MASK_DIAGNOSE, kernelHelper)
    diagnose = diagnose[5:6]
    diagnoseDec = int.from_bytes(diagnose, byteorder='big')
    print("diagnoseDec: " + str(diagnoseDec))

    reserve = bitwiseAnd(defines.MASK_RESERVE, kernelHelper)
    reserve = reserve[4:5]
    reserveDec = int.from_bytes(reserve, byteorder='big')
    print("reserveDec: " + str(reserveDec))

    time = bitwiseAnd(defines.MASK_TIME, kernelHelper)
    time = time[0:4]
    timeDec = int.from_bytes(time, byteorder='big')
    print("timeDec: " + str(timeDec))

    return [sensorStatusDec, interfaceModeDec, networkIdDec, diagnoseDec, reserveDec, timeDec]

def decodeObjectControlMessage(data):

    kernelHelper = np.copy(data)
    #print("KernelHelper:" + str(kernelHelper))
    numOfObjects = bitwiseAnd(defines.MASK_NUM_OF_OBJECTS, kernelHelper)
    numOfObjects = numOfObjects[7:8]
    numOfObjectsDec = int.from_bytes(numOfObjects, byteorder='big')
    print("numOfObjectsDec: " + str(numOfObjectsDec))

    numOfMessages = bitwiseAnd(defines.MASK_NUM_OF_MESSAGES, kernelHelper)
    numOfMessages = numOfMessages[6:7]
    numOfMessagesDec = int.from_bytes(numOfMessages, byteorder='big')
    print("numOfMessagesDec: " + str(numOfMessagesDec))

    cycleDuration = bitwiseAnd(defines.MASK_CYCLE_DURATION, kernelHelper)
    cycleDuration = cycleDuration[5:6]
    cycleDurationDec = int.from_bytes(cycleDuration, byteorder='big')
    print("cycleDurationDec: " + str(cycleDurationDec))

    objectData0format = bitwiseAnd(defines.MASK_OBJ_DATA0_FORMAT, kernelHelper)
    objectData0format = objectData0format[4:5]
    objectData0formatDec = int.from_bytes(objectData0format, byteorder='big')
    print("objectData0formatDec: " + str(objectData0formatDec))

    objectData1format = bitwiseAnd(defines.MASK_OBJ_DATA1_FORMAT, kernelHelper)
    objectData1format = objectData1format[4:5]
    objectData1formatDec = int.from_bytes(objectData1format, byteorder='big') >> 4
    print("objectData1formatDec: " + str(objectData1formatDec))

    cycleCount = bitwiseAnd(defines.MASK_CYCLE_COUNT, kernelHelper)
    cycleCount = cycleCount[0:4]
    cycleCountDec = int.from_bytes(cycleCount, byteorder='big')
    print("cycleCountDec: " + str(cycleCountDec))

    return [numOfObjectsDec, numOfMessagesDec, cycleDurationDec, objectData0formatDec, objectData1formatDec, cycleCountDec]

def decodeObjectData(data):

    kernelHelper = np.copy(data)
    #print("KernelHelper:" + str(kernelHelper))
    posX = bitwiseAnd(defines.MASK_POSX, kernelHelper)
    posX = posX[6:8]
    posXdec = int.from_bytes(posX, byteorder='big') >> 1
    posXdec = round((posXdec - 4096) * 0.128, 0)
    print("posXdec: " + str(posXdec))

    posY = bitwiseAnd(defines.MASK_POSY, kernelHelper)
    posY = posY[4:7]
    posYdec = int.from_bytes(posY, byteorder='big') >> 6
    posYdec = round((posYdec - 4096)*0.128, 0)
    print("posYdec: " + str(posYdec))

    velX = bitwiseAnd(defines.MASK_VELX, kernelHelper)
    velX = velX[3:5]
    velXdec = int.from_bytes(velX, byteorder='big') >> 3
    velXdec = round((velXdec - 1024) * 0.1 / 3.6, 0)
    print("velXdec: " + str(velXdec))

    velY = bitwiseAnd(defines.MASK_VELY, kernelHelper)
    velY = velY[1:4]
    velYdec = int.from_bytes(velY, byteorder='big') >> 6
    velYdec = round((velYdec - 1024) * 0.1 / 3.6, 0)
    print("velYdec: " + str(velYdec))

    objLen = bitwiseAnd(defines.OBJECT_LEN, kernelHelper)
    objLen = objLen[1:2]
    objLenDec = int.from_bytes(objLen, byteorder='big') >> 1
    objLenDec = round((objLenDec) * 0.2, 0)
    print("objLenDec: " + str(objLenDec))

    objId = bitwiseAnd(defines.OBJECT_ID, kernelHelper)
    objId = objId[0:1]
    objIdDec = int.from_bytes(objId, byteorder='big')
    print("objIdDec: " + str(objIdDec))

    return [objIdDec, objLenDec, posXdec, posYdec, velXdec, velYdec]

def bitwiseAnd(mask, data):
    andHelper = np.copy(data)
    anded = np.copy(data)
    for index in range(len(data)):
        anded[index] = mask[index] & andHelper[index]
    return anded