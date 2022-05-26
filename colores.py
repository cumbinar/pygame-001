#colores

import pygame
import sys
from pygame.locals import *  # se importan librerías

#dos formas de determinar color
color = (0, 140, 60)  #color con una tupla
colorDos = pygame.Color(255, 165, 0)  # color con un método

pygame.init()  # se inicia pygame

# define ancho y alto de la ventana
ventana = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Colores")  # se define el título

while True:
    ventana.fill(colorDos) #pinta la ventana con el color definido
    for evento in pygame.event.get():  # ciclo para dibujar la ventana
        if evento.type == QUIT:  # si el evento es click en la X de salir
            pygame.quit()
            sys.exit()
    
    pygame.display.update()  # se actualiza ventana
