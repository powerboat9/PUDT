import wave, pygame, base64, string, time, plysnd

TRANSMIT_SIZE = 100
LOWER_LIMIT = 17000
UPPER_LIMIT = 19000
SAMPLE_RATE = None

BIN_SIZE = UPPER_LIMIT - LOWER_LIMIT / 32
SECTION_PER_TRANSMIT = 3
SECTION_SIZE = TRANSMIT_SIZE / SECTION_PER_TRANSMIT

def setRange(mn, mx):
    if mn == None or (not isinstance(mn, int)) or (mx == None) or (not isinstance(mx, int)):
        raise ValueError()
    LOWER_LIMIT = 400
    UPPER_LIMIT = 600

def getNumFromB32(char):
    if char == None or (not isinstance(char, str)) or (len(char) > 1):
        raise ValueError("Not a 1 char string")
    ret = (string.ascii_uppercase + "234567").find(char)
    if ret == -1:
        raise ValueError("Could not translate " + char)
    return ret

def getSigOut(n):
    if n == None or (not isinstance(n, int)) or (not (0 <= n <= 31)) | ((n % 1) == 0):
        ValueError()
    return LOWER_LIMIT + BIN_SIZE * (n + 0.5)

def transmit(data, doWait):
    if data == None or (not isinstance(data, (bytes, bytearray))):
        raise Exception("Invalid transmision data")
    dataEncoded = base64.b32encode(data).replace(b"=", b"")
    freqList = ()
    for char in dataEncoded.decode("UTF-8"):
        freqList[len(freqList)] = getSigOut(getNumFromB32(char))
    plysnd.play(plysnd.getData(freqList, TRANSMIT_SIZE), doWait)