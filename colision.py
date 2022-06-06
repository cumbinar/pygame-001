#mover una imagen con el teclado

import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()



pygame.display.set_caption("CUMBI Perseguir un cuadrado con el teclado")

size = 800, 500
gris = 230, 230, 230
rojo = 255, 0, 0
naranja = 255, 155, 0
cuadrado_pos = [400, 400]
cuadrado2_pos =[100,100]
cuadrado_medida = [70, 70]
paso = 50

COLOR_FUENTE = (6, 47, 253)
screen = pygame.display.set_mode(size)

def dibujar_texto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 20)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    screen.blit(text, pos)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                cuadrado_pos[0] -= paso
            if event.key == K_RIGHT:
                cuadrado_pos[0] += paso
            if event.key == pygame.K_UP:
                cuadrado_pos[1] -= paso
            if event.key == pygame.K_DOWN:
               cuadrado_pos[1] += paso
        

    screen.fill(gris)
    dibujar_texto(screen, "Mueva el cuadrado ROJO con las teclas direccionales", [220, 30])
    cuadro2= pygame.draw.rect(screen, (naranja), (cuadrado2_pos[0], cuadrado2_pos[1], cuadrado_medida[0], cuadrado_medida[1]))
    cuadro1 = pygame.draw.rect(screen, (rojo),(cuadrado_pos[0], cuadrado_pos[1],cuadrado_medida[0], cuadrado_medida[1]))
    if cuadro1.colliderect(cuadro2): #detecta colision entre los dos cuadrados
        cuadrado2_pos[0] = randint(100, 700)
        cuadrado2_pos[1] = randint(100,400)

    
    pygame.display.update()
   
    
       


