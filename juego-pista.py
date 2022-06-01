import pygame
import random

NEGRO = (10, 8, 12)
COLOR_PISTA2 = (50, 58, 52)
BLANCO = (255, 255, 255)
NARANJA = (255, 165, 0)
ROJO = (255, 20, 20)
YELLOW = (255, 196, 0)
COLOR_FUENTE = (6, 47, 253)


def dibujar_texto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 50)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    screen.blit(text, pos)


def dibujar_pista(x_pista, ancho, color_pista):
    pygame.draw.rect(pantalla, color_pista, [
                     x_pista, 0, ancho, dimensiones[1]])
    for i in range(10, dimensiones[1], 20):
        pygame.draw.rect(pantalla, BLANCO, [234, i, 6, 8])


def rect_collider(objeto1, objeto2):
    colisiono = False
    if objeto2[0] + objeto2[2] > objeto1[0] and objeto2[0] < objeto1[0] + objeto1[2] and \
            objeto2[1] + objeto2[3] > objeto1[1] and objeto2[1] < objeto1[1] + objeto1[3]:
        colisiono = True
    return colisiono


pygame.init()

dimensiones = [480, 720]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Juego de Pista")

autos = [[185, 0, 35, 50], [255, -180, 35, 50],
         [185, -340, 35, 50], [255, -490, 35, 50]]
auto = [185, 600, 40, 54]

x_speed = 0
y_speed = 0

inicio_pista = 160
ancho_pista = 160

velocidad = random.randrange(1, 3)

game_over = False
salir = False
reloj = pygame.time.Clock()

while not salir:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salir = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                x_speed = -4
            if evento.key == pygame.K_RIGHT:
                x_speed = 4
            if evento.key == pygame.K_UP:
                y_speed = -4
            if evento.key == pygame.K_DOWN:
                y_speed = 4
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                x_speed = 0
            if evento.key == pygame.K_RIGHT:
                x_speed = 0
            if evento.key == pygame.K_UP:
                y_speed = 0
            if evento.key == pygame.K_DOWN:
                y_speed = 0
    pantalla.fill(NARANJA)
    dibujar_pista(inicio_pista, ancho_pista, NEGRO)
    pygame.draw.rect(pantalla, YELLOW, auto)
    if auto[0] > inicio_pista + 1 and (auto[0] + auto[2]) < (inicio_pista + ancho_pista) - 1:
        auto[0] += x_speed
    else:
        x_speed *= -1
        if (auto[0] + auto[2]) >= (inicio_pista + ancho_pista) - 1:
            auto[0] = (inicio_pista + ancho_pista) - auto[2] - 2
        elif auto[0] <= inicio_pista + 1:
            auto[0] = inicio_pista + 2

    auto[1] += y_speed
    for autoObjeto in autos:
        game_over = rect_collider(auto, autoObjeto)
        if game_over:
            salir = True
            break
        if autoObjeto[1] > dimensiones[1]:
            autoObjeto[1] = random.randrange(-150, -100)
        pygame.draw.rect(pantalla, ROJO, autoObjeto)
        autoObjeto[1] += velocidad
    velocidad += 0.0005
    pygame.display.flip()
    reloj.tick(60)

if game_over and salir:
    game_over = False
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        pantalla.fill(NARANJA)
        dibujar_pista(inicio_pista, ancho_pista, COLOR_PISTA2)
        dibujar_texto(pantalla, "Fin del Juego", [130, 350])
        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()
elif salir:
    pygame.quit()
