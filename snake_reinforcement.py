import pygame
from pygame.locals import *
import sys

#Pantalla inicial
pygame.init()
pantalla = pygame.display.set_mode((800,800))
pygame.display.set_caption("Snake")


print("camara armando")
while True:
    
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            sys.exit()
