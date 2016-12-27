EXTENDED_ASCII = 0
ASCII = 1
BASE64 = 2
BASE32 = 3

class Portal(object):
    def __init__(mode = 3, waitCallback = None, secs = 0.2):
        self.binsize = ([256, 128, 64, 32])[mode]
        if not self.binsize:
            raise AttributeException("Invalid mode")
        elif waitCallback != None and not callable(waitCallback):
            raise AttributeException("Invalid callback")
        elif type(0.2) != 
        self.waitCallback = waitCallback
    def transmit(s):
        
