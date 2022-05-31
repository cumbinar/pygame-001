#posicionar tres imágenes con randint

import sys
import pygame
from random import randint
# Inicializamos pygame
pygame.init()
# Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)
# Cambio el título de la ventana
pygame.display.set_caption("CUMBI posicionar tres imágenes con randint")
# Inicializamos variables
width, height = 800, 600
gris = 230, 230, 230
# Crea un objeto imagen y obtengo su rectángulo
cuadrado = pygame.image.load("imagenes/cuadro.png")
triangulo = pygame.image.load("imagenes/triangulo.png")
circulo = pygame.image.load("imagenes/ball.png")
# Comenzamos el bucle del juego
run = True
while run:
    # Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
    #pygame.time.delay(360)
    posx = randint(100,700)
    posy = randint(200,300)
    posx2 = randint(100, 700)
    posy2 = randint(200, 300)
    posx3 = randint(100, 700)
    posy3 = randint(200, 300)
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        #Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False
    # Muevo el rectángulo
  
    #Pinto el fondo de blanco, dibujo el rectángulo y actualizo la pantalla
    screen.fill(gris)
    pygame.time.delay(400)
    screen.blit(cuadrado, (posx,posy))
    screen.blit(triangulo, (posx2, posy2))
    screen.blit(circulo, (posx3, posy3))
    pygame.display.flip()
# Salgo de pygame
pygame.quit()
