"""This script implements the Cell class"""
import random


class Cell:
    """This class represents a cell. It has two possible states: dead or alive."""

    def __init__(self, percent: float) -> None:
        self.state = random.random() < percent  # The percent enables a given probability
        self.next_state: bool = False
        self.score: int = 0

    def update_state(self):
        """Compute the new state of the cell according to its score"""
        self.state = (self.score == 3) or (self.state and self.score == 2)

    def score_neighboors(self, score: int):
        """Store the score (number) of neighboors"""
        self.score = score
