#crear ventana con texto en barra

import pygame,sys
from pygame.locals import * #se importan librerías

pygame.init()  #se inicia pygame
ventana = pygame.display.set_mode((800,500)) #define ancho y alto de la ventana
pygame.display.set_caption("Hello Cumbi") #se define el título


while True:
    for evento in pygame.event.get():  #ciclo para dibujar la ventana
        if evento.type == QUIT:  #si el evento es click en la X de salir
            pygame.quit()
            sys.exit()
    pygame.display.update()  #se actualiza ventana
