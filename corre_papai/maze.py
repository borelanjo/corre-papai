class Maze:
    def __init__(self):
        # Mapa fixo por enquanto, no futuro pode ser gerado ou lido de arquivo
        self.grid = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]

    def is_walkable(self, x, y):
        """Retorna True se a posição for um caminho livre (0), False se for parede ou inválida."""
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            return self.grid[y][x] == 0
        return False

    def get_grid(self):
        """Retorna a matriz para renderização ou debug."""
        return self.grid
