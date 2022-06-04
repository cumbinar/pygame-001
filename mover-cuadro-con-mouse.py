import pygame, sys
pygame.init()

size = (800, 500)
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("Cumbi- Mover cuadrado con el mouse")

color_fuente = 0, 0, 0


def dibujar_texto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 25)
    text = fuente.render(texto, 1, color_fuente)
    screen.blit(text, pos)


#clock = pygame.time.clock()
gris = (230, 230, 230)
red = (255, 0, 0)

ciclo=True

while ciclo:
    for evento in pygame.event.get():
        if evento.type == pygame. QUIT:  # si el evento es click en la X de salir
            ciclo = False
            pygame.quit()
            sys.exit()
    
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    ventana.fill(gris)  # pinta la ventana con el color definido
    dibujar_texto(ventana, "Mover el cuadrado con el mouse", [250, 40])
    pygame.draw.rect(ventana, red, (x, y, 100, 100))

    pygame.display.update()  # se actualiza ventana
