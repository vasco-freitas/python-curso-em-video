import pygame
import time
pygame.mixer.init()

while True:
    pygame.mixer.music.load('hungria - quer andar de velar.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
