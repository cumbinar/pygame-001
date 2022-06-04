#dibujo de líneas aleatorias con cambio de longitud y color

import pygame
import sys
from random import randint
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Cumbi- Líneas aleatorias")

color_fuente = 0, 0, 0


def dibujar_texto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 25)
    text = fuente.render(texto, 1, color_fuente)
    screen.blit(text, pos)
    

gris = (230, 230, 230)

ciclo = True
while ciclo:
    ventana.fill(gris)  # pinta la ventana con el color definido
    dibujar_texto(ventana, "Líneas aleatorias variando longitud y color", [250, 40])
   
    xi = randint(100, 700)
    yi = randint(100, 400)
    xf = randint(100, 700)
    yf = randint(100, 400)
   
    
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
  
    pygame.draw.line(ventana, (r, g, b), (xi, yi), (xf, yf), 3)
    pygame.time.delay(300)
    

    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT:  # si el evento es click en la X de salir
            ciclo = False
            pygame.quit()
            sys.exit()

    pygame.display.update()  # se actualiza ventana
