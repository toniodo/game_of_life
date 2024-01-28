"""This script implement the basic version of the game of life"""
import matplotlib.pyplot as plt
from grid import Grid

WIDTH = 100
LENGTH = 150
NB_ITER = 100
PERCENT = 0.1 # Percentage of initial alive cells


def main():
    """A global function to execute the game of life"""
    # Create grid
    grid = Grid(LENGTH, WIDTH, PERCENT)
    # Create figure
    _, ax = plt.subplots()
    for _ in range(NB_ITER):
        # Compute scores
        grid.compute_scores()
        # Load new state
        grid.update_states()
        visual_grid = grid.grid_values()
        # Clear the previous result
        ax.clear()
        # Plot the result (white: dead cell, black: alive cell)
        ax.imshow(1-visual_grid, cmap='gray', interpolation='none')
        plt.pause(0.7)
        plt.show(block=False)


# Call the main function
main()
