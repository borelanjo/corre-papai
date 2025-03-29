import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Cria a janela
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Corre, Papai!")

# Cores
BRANCO = (255, 255, 255)
AZUL = (50, 150, 255)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche o fundo
    tela.fill(BRANCO)

    # Desenha um retângulo (como se fosse o pai)
    pygame.draw.rect(tela, AZUL, (300, 220, 40, 40))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
sys.exit()
