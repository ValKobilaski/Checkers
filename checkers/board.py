import pygame
from .constants import BOARD_BEIGE, BOARD_BROWN, ROWS, SQUARE_SIZE


class Board:
    def __init__(self):
        self.board = [[]]
        self.selectedPiece = None
        self.whiteLeft = 12
        self.blackLeft = 12
        self.whiteKings = 0
        self.blackKings = 0

    def draw_squares(self, win):
        win.fill(BOARD_BROWN)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(
                    win,
                    BOARD_BEIGE,
                    (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )
