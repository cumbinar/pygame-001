#animar uuna imagen png con un ciclo iterativo

import sys
import pygame
# Inicializamos pygame
pygame.init()
# Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)
# Cambio el título de la ventana
pygame.display.set_caption("CUMBI Mover cuadrado")
# Inicializamos variables
width, height = 800, 600
speed = [5, 3]
gris = 230, 230, 230
# Crea un objeto imagen y obtengo su rectángulo
cuadrado = pygame.image.load("imagenes/cuadro.png")
cuadradorect = cuadrado.get_rect()
# Comenzamos el bucle del juego
run = True
while run:
    # Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
    pygame.time.delay(30)
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        #Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False
    # Muevo el rectángulo
    cuadradorect = cuadradorect.move(speed)
    if cuadradorect.left < 0 or cuadradorect.right > width:
        speed[0] = -speed[0]
    if cuadradorect.top < 0 or cuadradorect.bottom > height:
        speed[1] = -speed[1]    
    #Pinto el fondo de blanco, dibujo el rectángulo y actualizo la pantalla
    screen.fill(gris)
    screen.blit(cuadrado, cuadradorect)
    pygame.display.flip()
# Salgo de pygame
pygame.quit()