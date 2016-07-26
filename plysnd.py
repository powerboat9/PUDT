import pygame

SAMPLE_RATE = None

def getData(freqList, miliSecs, sampleRatePerSec):
    nSamples = freqList.length * miliSecs * sampleRatePerSec / 1000
    data = chararray()
    for n in range(nSamples):
        data.append(

def play(data, doWait):
    if v == None:
        pygame.mixer.init()
        v = pygame.mixer.get_init()
        SAMPLE_RATE = v[0]
    transmitSound = pygame.mixer.Sound(data)
    transmitSound.play()
    if doWait:
        time.sleep(transmitSound.get_length())
