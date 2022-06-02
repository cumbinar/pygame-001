#dibujo de líneas aleatorias con cambio de longitud y color

import pygame
import sys
from random import randint
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Cumbi- Líneas aleatorias")


color = pygame.Color(70, 80, 150)
colorDos = pygame.Color(255, 165, 0)
colorTres = pygame.Color(255, 0, 68)
colorCuatro = pygame.Color(0, 0, 0)
colorCinco = pygame.Color(240, 240, 240)
#pygame.draw.line(ventana, color, (100,100),(600,400), 5) #método dibujar línea, ventana,color coordenadas

ciclo = True
while ciclo:
    ventana.fill(colorCinco)  # pinta la ventana con el color definido
    # método dibujar línea, ventana,color coordenadas
    #dibujar = 7
    xi = randint(100, 700)
    yi = randint(100, 400)
    xf = randint(100, 700)
    yf = randint(100, 400)
   
    
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
  
    pygame.draw.line(ventana, (r, g, b), (xi, yi), (xf, yf), 3)
    pygame.time.delay(200)
    

    for evento in pygame.event.get():  # ciclo para dibujar la ventana
        if evento.type == QUIT:  # si el evento es click en la X de salir
            ciclo = False
            pygame.quit()
            sys.exit()

    pygame.display.update()  # se actualiza ventana
