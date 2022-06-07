#Fondo en movimiento

import sys
import pygame
pygame.init()
# Muestro una ventana de 800x500
size = 800, 500
screen = pygame.display.set_mode(size)
# Cambio el título de la ventana
pygame.display.set_caption("CUMBI Fondo en movimiento")
# Inicializamos variables

# Crea fondo
fondo = pygame.image.load("imagenes/fondo-1.jpg").convert() #carga y optimiza imagen

x = 0


# Comenzamos el bucle del juego
run = True
while run:
  
    for event in pygame.event.get():
        #Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False

    
    #Pinto el fondo de la pantalla
    screen.blit(fondo, (x, 0))
    pygame.display.flip()
# Salgo de pygame
pygame.quit()
