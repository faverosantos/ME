
# Flags de controle de fluxo de software
DEBUG_MODE = True

# Dados importantes para o protocolo do Doppler
'Fonte: 2019-02-22_Doc_Data Communication UMRR Traffic Management_UMRR0C'
HEADER = bytearray([0xCA, 0xCB, 0xCC, 0xCD])
FOOTER = bytearray([0xEA, 0xEB, 0xEC, 0xED])
OBJECT_CONTROL = bytearray([0x05, 0x01])
OBJECT_DATA_1 = bytearray([0x05, 0x02])
OBJECT_DATA_2 = bytearray([0x05, 0x03])
SYNC_MESSAGE = bytearray([0x02, 0xFF])
SENSOR_CONTROL = bytearray([0x05, 0x00])

REFRESH_TIME_MS = 0.5

