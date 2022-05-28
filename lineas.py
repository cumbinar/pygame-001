#dibujar líneas con diferentes colores

import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Cumbi- Líneas")


color = pygame.Color(70, 80, 150)
colorDos = pygame.Color(255, 165, 0)
colorTres = pygame.Color(255, 0, 68)
colorCuatro = pygame.Color(0,0,0)
#pygame.draw.line(ventana, color, (100,100),(600,400), 5) #método dibujar línea, ventana,color coordenadas
print (color.r) #imprime los valores rgb en pantalla
print (color.g)
print (color.b)

while True:
    ventana.fill(colorDos)  # pinta la ventana con el color definido
    pygame.draw.line(ventana, color, (100,100),(600,400), 3) #método dibujar línea, ventana,color coordenadas
    pygame.draw.line(ventana, colorTres, (600, 400), (600, 100), 3)
    pygame.draw.line(ventana, colorCuatro, (600, 100),(300, 100), 3)
    for evento in pygame.event.get():  # ciclo para dibujar la ventana
        if evento.type == QUIT:  # si el evento es click en la X de salir
            pygame.quit()
            sys.exit()

    pygame.display.update()  # se actualiza ventana
