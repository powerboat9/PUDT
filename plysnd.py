import pygame, math
import numpy as np

SAMPLE_RATE = 192000

def split(n):
    n1 = n >> 8
    n2 = n - (n1 << 8)
    return (n2, n1)#Little edian

def setSampleRate(n):
    SAMPLE_RATE = n

def getData(freqList, miliSecs):
    arrayLen = len(freqList) * miliSecs / 1000 * SAMPLE_RATE
    data = np.zeros(arrayLen, dtype=np.int16)
    for freqN in range(len(freqList)):
        freq = freqList[freqN]
        secs = miliSecs / 1000
        numSamples = np.floor(secs * SAMPLE_RATE)
        samplesPerFreq = np.floor(numSamples / (secs * freq))#numSamples / (secs / freq)
        for sample in range(numSamples):
            v = np.sin(math.pi * 2 * ((sample % samplesPerFreq) / samplesPerFreq))
            data[(freqN + 1) * (sample + 1) - 1] = v
    return data.tobytes()

def play(data, doWait):
    if v == None:
        pygame.mixer.init(frequency = 192000)
        v = pygame.mixer.get_init()
    transmitSound = pygame.mixer.Sound(data)
    transmitSound.play()
    if doWait:
        time.sleep(transmitSound.get_length())
