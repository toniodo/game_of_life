"""This script implements the Grid class"""
import numpy as np
from cell import Cell


class Grid:
    """Representation of the grid of cells"""

    def __init__(self, length, width, percent: float = 0.5):
        self.length = length
        self.width = width
        self.grid = np.array([[Cell(percent) for _ in range(length)] for _ in range(width)])

    def in_grid(self, i: int, j: int):
        """Return if the point is in the grid"""
        return 0 <= i <= self.width - 1 and 0 <= j <= self.length - 1

    def compute_scores(self):
        """Compute scores for each cell"""
        for i in range(self.width):
            for j in range(self.length):
                score = 0
                # We explore all the adjacents cells
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if (not (di == 0 and dj == 0) and
                            self.in_grid(i + di, j + dj) and
                                self.grid[i + di, j + dj].state):
                            score += 1
                self.grid[i, j].score_neighboors(score)

    def update_states(self):
        """Update the state for each cell"""
        for i in range(self.width):
            for j in range(self.length):
                self.grid[i, j].update_state()

    def grid_values(self):
        """Return the grid with all the values"""
        values = np.full((self.width, self.length), False)
        # values = np.array([[False for _ in range(self.length)] for _ in range(self.width)])
        for i in range(self.width):
            for j in range(self.length):
                values[i, j] = self.grid[i, j].state
        return values
