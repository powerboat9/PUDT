import pygame

def play(data, doWait):
    if v == None:
        pygame.mixer.init()
        v = pygame.mixer.get_init()
        SAMPLE_RATE = v[0]
    transmitSound = pygame.mixer.Sound(data)
    transmitSound.play()
    if doWait:
        time.sleep(transmitSound.get_length())
