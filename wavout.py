import numpy as np
import wave

# heavily modified from swood by creator of swood (He tried to avoid taking credit)
# https://github.com/milkey-mouse/swood

def savewav(filename, data, framerate=192000):
    with wave.open(filename, "wb") as wav:
        wav.setparams((1,  # channels
                        data.itemsize,  # sample width
                        framerate,  # sample rate
                        len(data),  # number of frames
                        "NONE", "not compressed"))  # compression type (none are supported)
        wav.writeframesraw(data)