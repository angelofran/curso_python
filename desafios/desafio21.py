import pygame

pygame.init()
pygame.mixer.music.load('title.mp3')
pygame.mixer.music.play()
pygame.event.wait()