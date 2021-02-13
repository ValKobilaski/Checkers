import pygame
from .constants import BOARD_BEIGE, BOARD_BROWN, ROWS, COLS, SQUARE_SIZE, WHITE, BLACK
from .piece import Piece


class Board:
    def __init__(self):
        self.board = [[]]
        self.selectedPiece = None
        self.whiteLeft = 12
        self.blackLeft = 12
        self.whiteKings = 0
        self.blackKings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BOARD_BROWN)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(
                    win,
                    BOARD_BEIGE,
                    (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = (
            self.board[row][col],
            self.board[piece.row][piece.col],
        )

        piece.move(row, col)
        if row == ROWS or row == 0:
            piece.make_king()
            if piece.colour == WHITE:
                self.whiteKings += 1
            else:
                self.blackKings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):

                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
