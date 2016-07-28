import udtlib as udt
import plysnd
import numpy as np
from wavout import savewav
import wave

data = plysnd.getData((16000, 15000, 7000), 5000)

savewav("tmp.wav", data)

plysnd.play(data, True)