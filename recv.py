EXTENDED_ASCII = 0
ASCII = 1
BASE64 = 2
BASE32 = 3

class Portal(object):
    def __init__(mode = 3, waitCallback = None):
        self.binsize = ([256, 128, 64, 32])[mode]
        if not self.binsize:
            raise AttributeException("Invalid mode")
        elif waitCallback != None and not callable(waitCallback):
            raise AttributeException("Invalid callback")
        self.waitCallback = waitCallback
    def transmit(s):
        
