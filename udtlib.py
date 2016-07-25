import wave, pygame, base64, string, time

TRANSMIT_SIZE = 100
LOWER_LIMIT = 17000
UPPER_LIMIT = 19000

BIN_SIZE = UPPER_LIMIT - LOWER_LIMIT / 32
SECTION_PER_TRANSMIT = 3
SECTION_SIZE = TRANSMIT_SIZE / SECTION_PER_TRANSMIT

def setRange(mn, mx):
    if mn == None || !isinstance(mn, int) || mx == None || !isinstance(mx, int):
        raise ValueError()
    LOWER_LIMIT = 400
    UPPER_LIMIT = 600

def getNumFromB32(char):
    if char == None || !isinstance(char, str) || (char.length > 1):
        raise ValueError()
    ret = (string.lowercase + "234567").find(char)
    if ret == -1:
        raise ValueError()
    return ret

def getSigOut(n):
    if n == None || !isinstance(n, int) || !(0 <= n <= 31) || ((n % 1) == 0):
        ValueError()
    return LOWER_LIMIT + BIN_SIZE * (n + 0.5)

def transmit(data):
    if data == None || !isinstance(data, (bytes, bytearray)):
        raise Exception("Invalid transmision data")
    dataEncoded = base64.b32encode(data).replace(b"=", "")
    freqList = bytearray()
    for char in dataEncoded:
        freqList.append(getSigOut(getNumFromB32(char)))
    transmitSound = pygame.mixer.Sound(freqList)
    transmitSound.play()
    time.sleep(transmitSound.get_length())