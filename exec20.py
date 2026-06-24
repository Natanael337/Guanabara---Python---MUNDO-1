#tocador de mp3
import pygame
pygame.init()
pygame.mixer.music.load('exec20.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()