import pygame, math, time
import numpy as np

SAMPLE_RATE = 192000

def split(n):
    n1 = n >> 8
    n2 = n - (n1 << 8)
    return (n2, n1)#Little edian

def setSampleRate(n):
    SAMPLE_RATE = n

def getData(freqList, miliSecs):
    arrayLen = int(np.floor(len(freqList) * miliSecs / 1000 * SAMPLE_RATE))
    data = np.zeros(arrayLen, dtype=np.int16)
    dataInsert = 0
    freqL = len(freqList)
    for freqN in range(freqL):
        freq = freqList[freqN]
        secs = miliSecs / 1000
        numSamples = int(np.floor(secs * SAMPLE_RATE))
        samplesPerFreq = int(np.floor(numSamples / (secs * freq)))#numSamples / (secs / freq)
        tempData = np.zeros(samplesPerFreq, dtype=np.int16)
        for i in range(samplesPerFreq):
            v = 32767 * np.sin(math.pi * 2 * (i / samplesPerFreq))
            tempData[i] = v
            print("Generated tone part {} of {} for tone {} of {}".format(i + 1, samplesPerFreq, freqN + 1, freqL))
        numFreqIters = int(np.floor(secs * freq))
        cp = range(dataInsert, dataInsert + (numFreqIters - 1) * samplesPerFreq + 1, samplesPerFreq)
        print("Inserting {} to {}".format(cp[0], cp[len(cp) - 1]))
        data = np.insert(data, cp, tempData)
        dataInsert += numSamples
    return data.tobytes()

def play(data, doWait):
    v = pygame.mixer.get_init()
    if v == None:
        pygame.mixer.init(frequency = 192000)
        v = pygame.mixer.get_init()
    transmitSound = pygame.mixer.Sound(data)
    transmitSound.play()
    if doWait:
        t = transmitSound.get_length()
        print(t)
        time.sleep(t)