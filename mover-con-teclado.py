#mover una imagen con el teclado

import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

size = 800, 600

pygame.display.set_caption("CUMBI Mover cuadrado con el teclado")
screen = pygame.display.set_mode(size)

cuadrado = pygame.image.load("imagenes/cuadro.png")

posx = 300
posy = 300

velocidad = 10
width, height = 800, 600
color = pygame.Color(230, 230, 230)

derecha = True

run = True
while run:
    screen.fill(color)
    screen.blit(cuadrado, (posx, posy))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                posx -= velocidad
            elif event.key == K_RIGHT:
                posx += velocidad
                
pygame.display.update()                    

