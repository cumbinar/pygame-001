#Fondo en movimiento

import sys
import pygame
pygame.init()
# Muestro una ventana de 800x500
ancho = 800
alto = 500
screen = pygame.display.set_mode((ancho, alto))
fps = 120 #variable para mostrar cuadros por segundo
reloj = pygame.time.Clock() #variable para el reloj
# Cambio el título de la ventana
pygame.display.set_caption("CUMBI Fondo en movimiento")
# Inicializamos variables

# Crea fondo
fondo = pygame.image.load("imagenes/fondo-1.jpg").convert() #carga y optimiza imagen

x = 0 # variable para la coordenada X
# Comenzamos el bucle del juego
run = True
while run:
  
    for event in pygame.event.get():
        #Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    x_relativa = x % fondo.get_rect().width #devuelve el resto de dividir x / ancho del fondo
    #Pinto el fondo de la pantalla
    screen.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < ancho:
        screen.blit(fondo, (x_relativa,0))
    x -= 1
    pygame.display.flip()
    reloj.tick(fps) #llama al reloj y pasa los cuadros por minuto
# Salgo de pygame
pygame.quit()
