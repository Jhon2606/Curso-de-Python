import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('testemusica.mp3')
pygame.mixer.music.play()
pygame.event.wait()