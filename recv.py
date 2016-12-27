import random

EXTENDED_ASCII = 0
ASCII = 1
BASE64 = 2
BASE32 = 3
BASE16 = 4
BASE8 = 5

class Portal(object):
    def __init__(mode = 3, waitCallback = None, secs = 0.2):
        self.bins = ([256, 128, 64, 32, 16, 8])[mode]
        if not self.bins:
            raise AttributeException("Invalid mode")
        elif waitCallback != None and not callable(waitCallback):
            raise AttributeException("Invalid callback")
        elif type(secs) != "<class 'int'>":
            raise AttributeException("Invalid frequency duration")
        self.waitCallback = waitCallback
        self.secs = secs
    def raw_transmit(transmitList, minfreq, maxfreq):
        binsize = (maxfreq - minfreq) / self.bins
        for freq in transmitList
