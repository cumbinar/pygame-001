#dibujo de líneas por iteración

import pygame
import sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Cumbi- Multilíneas")


color = pygame.Color(70, 80, 150)
colorDos = pygame.Color(255, 165, 0)
colorTres = pygame.Color(255, 0, 68)
colorCuatro = pygame.Color(0, 0, 0)
colorCinco = pygame.Color(240, 240, 240)
#pygame.draw.line(ventana, color, (100,100),(600,400), 5) #método dibujar línea, ventana,color coordenadas


while True:
    ventana.fill(colorCinco)  # pinta la ventana con el color definido
    # método dibujar línea, ventana,color coordenadas
    dibujar = 7
    xi = 300
    yi = 100
    xf = 300
    yf = 400
    r = 0
    g = 0
    b = 0
    for ciclo in range(dibujar):
        pygame.draw.line(ventana, (r,g,b), (xi, yi), (xf, yf), 3)
        yi = yi + 50
        xf = xf + 50
        r += 2
        g += 35
        b += 20

    for evento in pygame.event.get():  # ciclo para dibujar la ventana
        if evento.type == QUIT:  # si el evento es click en la X de salir
            pygame.quit()
            sys.exit()

    pygame.display.update()  # se actualiza ventana
