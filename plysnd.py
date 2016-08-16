import pygame, time
from math import pi
import numpy as np

SAMPLE_RATE = 192000

def split(n):
    n1 = n >> 8
    n2 = n - (n1 << 8)
    return (n2, n1)#Little edian

def setSampleRate(n):
    SAMPLE_RATE = n

def genTonePattern(freq, secs, sampleRate=192000):
    numSamples = int(np.floor(sampleRate * secs))
    secs = numSamples / sampleRate
    iters = freq * secs
    timeToPlayIteration = 1 / freq
    samplesPerFreq = 
    data = np.empty(numSamples, dtype = np.int16)
    for 

def getData(freqList, miliSecs):
    arrayLen = int(np.floor(len(freqList) * miliSecs / 1000 * SAMPLE_RATE))
    data = np.zeros(arrayLen, dtype=np.int16)
    dataInsert = 0
    freqL = len(freqList)
    for freqN in range(freqL):
        freq = freqList[freqN]
        secs = miliSecs / 1000
        numSamples = int(np.floor(secs * SAMPLE_RATE))
        numFreqIters = int(np.floor(secs * freq))
        samplesPerFreq = int(np.floor(numSamples / numFreqIters))#numSamples / (secs / freq)
        tempData = np.zeros(samplesPerFreq, dtype=np.int16)
        for i in range(samplesPerFreq):
            v = 32767 * np.sin(pi * 2 * (i / samplesPerFreq))
            tempData[i] = v
            print("Generated tone part {} of {} for tone {} of {}".format(i + 1, samplesPerFreq, freqN + 1, freqL))
        cp = range(dataInsert, dataInsert + (numFreqIters - 1) * samplesPerFreq, samplesPerFreq)
        print("Inserting {} to {}".format(cp[0], cp[len(cp) - 1]))
        data = np.insert(data, cp, tempData)
        dataInsert += numSamples
    return data

def play(data, doWait):
    v = pygame.mixer.get_init()
    if v == None:
        pygame.mixer.init(frequency = 192000)
        v = pygame.mixer.get_init()
    transmitSound = pygame.mixer.Sound(data.tobytes())
    transmitSound.play()
    if doWait:
        t = transmitSound.get_length()
        print(t)
        time.sleep(t)
