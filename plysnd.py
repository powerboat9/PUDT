import pygame

SAMPLE_RATE = None

def split(n):
    n1 = n >> 8
    n2 = n - (n1 << 8)
    return (n2, n1)#Little edian

def getData(freqList, miliSecs, sampleRatePerSec):
    nSamples = freqList.length * miliSecs / 1000 * sampleRatePerSec
    data = chararray()
    for n in range(nSamples):
        
        freq = 
        data.append(splt[0])
        data.append(splt[1])

def play(data, doWait):
    if v == None:
        pygame.mixer.init()
        v = pygame.mixer.get_init()
        SAMPLE_RATE = v[0]
    transmitSound = pygame.mixer.Sound(data)
    transmitSound.play()
    if doWait:
        time.sleep(transmitSound.get_length())
