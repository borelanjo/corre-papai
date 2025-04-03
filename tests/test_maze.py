import unittest
from corre_papai.maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.maze = Maze()

    def test_maze_dimensions(self):
        grid = self.maze.get_grid()
        self.assertEqual(len(grid), 5)
        self.assertTrue(all(len(row) == 5 for row in grid))

    def test_walkable_path(self):
        self.assertTrue(self.maze.is_walkable(1, 1))  # caminho
        self.assertFalse(self.maze.is_walkable(0, 0))  # parede
        self.assertFalse(self.maze.is_walkable(99, 99))  # fora do grid

if __name__ == '__main__':
    unittest.main()
