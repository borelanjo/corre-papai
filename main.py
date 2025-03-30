import pygame
import sys

# Inicializa o Pygame
pygame.init()

# ----- Maze map -----
# 1 = wall, 0 = path
maze = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# ----- Posição inicial do pai (jogador) -----
player_x = 1  # coluna
player_y = 1  # linha

# Apenas para visualizar no terminal
for row in maze:
    print(row)

# Configurações iniciais da tela
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Corre, Papai!")
clock = pygame.time.Clock()

directions = {
    pygame.K_LEFT:  (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP:    (0, -1),
    pygame.K_DOWN:  (0, 1)
}

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        # Captura teclas pressionadas
        keys = pygame.key.get_pressed()

        for key, (dx, dy) in directions.items():
            if keys[key]:
                new_x = player_x + dx
                new_y = player_y + dy

                # Verifica se está dentro dos limites da matriz
                if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]):
                    if maze[new_y][new_x] == 0:
                        player_x, player_y = new_x, new_y
                break  # só permite um movimento por vez

        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Preenche o fundo com branco

    # ----- Desenha o labirinto -----
    block_size = 40  # Tamanho do quadrado (em pixels)

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(
                    screen,
                    (100, 100, 100),  # cor da parede
                    (x * block_size, y * block_size, block_size, block_size)
                )

    # ----- Desenha o pai (jogador) -----
    pygame.draw.rect(
        screen,
        (50, 150, 255),  # cor azul
        (player_x * block_size, player_y * block_size, block_size, block_size)
    )



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
