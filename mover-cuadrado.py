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
blue = 0, 170, 228
# Crea un objeto imagen y obtengo su rectángulo
cuadrado = pygame.image.load("cuadro.png")
cuadradorect = cuadrado.get_rect()
# Comenzamos el bucle del juego
run = True
while run:
    # Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
    pygame.time.delay(20)
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        #Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:run = False
    # Muevo la pelota
    cuadradorect = cuadradorect.move(speed)
    if cuadradorect.left < 0 or cuadradorect.right > width:
        speed[0] = -speed[0]
    if cuadradorect.top < 0 or cuadradorect.bottom > height:
        speed[1] = -speed[1]    
    #Pinto el fondo de blanco, dibujo la pelota y actualizo la pantalla
    screen.fill(blue)
    screen.blit(cuadrado, cuadradorect)
    pygame.display.flip()
# Salgo de pygame
pygame.quit()