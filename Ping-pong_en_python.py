import pygame
import random

pygame.init()

# Colores
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

#ventana
width = 800
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PING-PONG")

# tiempo
clock = pygame.time.Clock()

# Dimensiones de los jugadores
player_width = 10
player_height = 100

# Jugador 1: coordenadas y velocidad
x_player1 = 20
y_player1 = 200
player1_speed = 0

# Jugador 2: coordenadas y velocidad
x_player2 = 770
y_player2 = 200
player2_speed = 0.5

# Bola: coordenadas y velocidad
x_ball = 390
y_ball = 250
x_ball_speed = 5
y_ball_speed = 5

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Lógica para mover automáticamente al jugador 2
    if x_ball > width // 2 and x_ball_speed > 0:
        if y_player2 + player_height // 2 < y_ball:
            player2_speed = 2  # Mueve hacia abajo
        elif y_player2 + player_height // 2 > y_ball:
            player2_speed = -2  # Mueve hacia arriba
        else:
            player2_speed = 0
    else:
        player2_speed = 0

    # Teclas para controlar jugador 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_speed = -3
    elif keys[pygame.K_s]:
        player1_speed = 3
    else:
        player1_speed = 0

    # Limitar movimiento de los jugadores
    if y_player1 > height - player_height:
        y_player1 = height - player_height
    elif y_player1 < 0:
        y_player1 = 0

    if y_player2 > height - player_height:
        y_player2 = height - player_height
    elif y_player2 < 0:
        y_player2 = 0

    # Condiciones para límites de la bola
    if x_ball > width:
        # La bola sale de la pantalla, reiniciar posición en el centro
        x_ball = width // 2
        y_ball = height // 2
        x_ball_speed = 4
        y_ball_speed = 4

    if x_ball < 0:
        # La bola sale de la pantalla, reiniciar posición en el centro
        x_ball = width // 2
        y_ball = height // 2
        x_ball_speed = -4
        y_ball_speed = 4

    if y_ball > height - 10 or y_ball < 10:
        y_ball_speed = -y_ball_speed

    # Mover jugador
    y_player1 += player1_speed
    y_player2 += player2_speed

    # Mover la bola
    x_ball += x_ball_speed
    y_ball += y_ball_speed

    # Dibujar la pantalla
    screen.fill(green)

    # Dibujar jugadores
    player_1 = pygame.draw.rect(screen, blue, (x_player1, y_player1, player_width, player_height))
    player_2 = pygame.draw.rect(screen, red, (x_player2, y_player2, player_width, player_height))

    # Dibujar la bola
    ball = pygame.draw.circle(screen, white, (x_ball, y_ball), 10)

    # Colisiones
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        x_ball_speed = -x_ball_speed

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
