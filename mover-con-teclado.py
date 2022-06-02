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
COLOR_FUENTE = (6, 47, 253)
#derecha = True


def dibujar_texto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 30)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    screen.blit(text, pos)


run = True
while run:
    screen.fill(color)
    dibujar_texto(screen, "Mueva el cuadrado con las teclas direccionales", [150, 50])
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
            elif event.key == pygame.K_UP:
                posy -= velocidad
            elif event.key == pygame.K_DOWN:
                posy += velocidad
                
pygame.display.update()                    

