import wave, pygame, base64

TRANSMIT_SIZE = 100

SECTION_PER_TRANSMIT = 3
SECTION_SIZE = TRANSMIT_SIZE / SECTION_PER_TRANSMIT

def transmit(data, encoding = None):
    if data == None || !isinstance(data, ):
        raise Exception("Invalid transmision data")
    if encoding == None:
        