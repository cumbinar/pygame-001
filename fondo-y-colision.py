#Fondo en movimiento
import pygame
import sys
from pygame.locals import *
from random import randint
import time

pygame.init()
# Muestro una ventana de 800x500
ancho = 800
alto = 500
screen = pygame.display.set_mode((ancho, alto))
fps = 120  # variable para mostrar cuadros por segundo
reloj = pygame.time.Clock()  # variable para el reloj
# Cambio el título de la ventana
pygame.display.set_caption("CUMBI Fondo en movimiento y colisióm")
# Inicializamos variables
rojo = 255, 0, 0
naranja = 255, 155, 0
cuadrado_pos = [400, 400]
cuadrado2_pos = [100, 100]
cuadrado_medida = [70, 70]
cuadrado_rojo_medida = [50, 50]

color_fuente = (6, 47, 253)
paso = 50
# Crea fondo
# carga y optimiza imagen
fondo = pygame.image.load("imagenes/fondo-1.jpg").convert()

x = 0  # variable para la coordenada X
# Comenzamos el bucle del juego


def dibujar_texto(screen, texto, pos):
    fuente = pygame.font.SysFont('arial', 16)
    text = fuente.render(texto, 1, color_fuente)
    screen.blit(text, pos)



run = True
while run:

    for event in pygame.event.get():
        #Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                cuadrado_pos[0] -= paso
            if event.key == K_RIGHT:
                cuadrado_pos[0] += paso
            if event.key == pygame.K_UP:
                cuadrado_pos[1] -= paso
            if event.key == pygame.K_DOWN:
               cuadrado_pos[1] += paso        

    # devuelve el resto de dividir x / ancho del fondo
    x_relativa = x % fondo.get_rect().width
    #Pinto el fondo de la pantalla
    screen.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < ancho:
        screen.blit(fondo, (x_relativa, 0))
    x -= 1
    
    reloj.tick(fps)  # llama al reloj y pasa los cuadros por minuto
# Salgo de pygame
    dibujar_texto(screen, "Mueva el cuadrado ROJO con las teclas direccionales", [220, 10])



    cuadro2 = pygame.draw.rect(screen, (naranja), (cuadrado2_pos[0], cuadrado2_pos[1], cuadrado_medida[0], cuadrado_medida[1]))
    cuadro1 = pygame.draw.rect(
        screen, (rojo), (cuadrado_pos[0], cuadrado_pos[1], cuadrado_rojo_medida[0], cuadrado_rojo_medida[1]))

   

    if cuadro1.colliderect(cuadro2):  # detecta colision entre los dos cuadrados
        cuadrado_rojo_medida[0] += 5
        cuadrado_rojo_medida[1] += 5
        pygame.mixer.music.load('imagenes/clap.wav')
        pygame.mixer.music.play()
        cuadrado2_pos[0] = randint(100, 700)
        cuadrado2_pos[1] = randint(100, 400)

    if cuadrado_rojo_medida[0] == 200:
        dibujar_texto(screen, "Nuevo Juego ", [100, 100])
        pygame.mixer.music.load('imagenes/kick.WAV')
        pygame.mixer.music.play(3)
        pygame.display.update()
        time.sleep(8)
        cuadrado_rojo_medida[0] = 50
        cuadrado_rojo_medida[1] = 50   
      
    pygame.display.update()
pygame.quit()
