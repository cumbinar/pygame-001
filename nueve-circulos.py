#matriz de círculos en escala de grises

from tkinter import Y
import pygame
import sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Cumbi- Matriz de círculos")


color = pygame.Color(70, 80, 150)
colorDos = pygame.Color(255, 165, 0)
colorTres = pygame.Color(255, 0, 68)
colorCuatro = pygame.Color(0, 0, 0)
colorCinco = pygame.Color(240, 240, 240)
#pygame.draw.line(ventana, color, (100,100),(600,400), 5) #método dibujar línea, ventana,color coordenadas


while True:
    ventana.fill(colorCinco)  # pinta la ventana con el color definido
    # método dibujar línea, ventana,color coordenadas
    #pygame.draw.circle(ventana, color, (100, 100), 50)
    dibujar = 9
    x_centro = 0
    y_centro = 0
    y_centro1 = 0
    y_centro2 = 0
    r = 0
    
    for ciclo in range(dibujar):
        #pygame.draw.circle(ventana, (r, g, b), (x_centro, y_centro), 20)
        #pygame.draw.line(ventana, (r, g, b), (xi, yi), (xf, yf), 3)
        
        if ciclo >= 0 and ciclo <= 2:
            x_centro = 100
            y_centro += 50
            r += 15      
            pygame.draw.circle(ventana, (r, r, r), (x_centro, y_centro), 20)
        if ciclo >= 3 and ciclo <= 5:
            x_centro = 150
            y_centro1 += 50     
            r += 15
            pygame.draw.circle(ventana, (r, r, r), (x_centro, y_centro1), 20)
        if ciclo >= 6 and ciclo <= 8:
            x_centro = 200
            y_centro2 += 50 
            r += 15
            pygame.draw.circle(ventana, (r, r, r), (x_centro, y_centro2), 20)
       
    for evento in pygame.event.get():  # ciclo para dibujar la ventana
        
        if evento.type == QUIT:  # si el evento es click en la X de salir
            pygame.quit()
            sys.exit()

    pygame.display.update()  # se actualiza ventana
