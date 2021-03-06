import pygame

# Display shape
WIDTH = 800
HEIGHT = 800

# Board shape
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS

# RGB colour codes
RED = (255, 0, 0)
GREEN = (255, 0, 0)
BLUE = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BOARD_BEIGE = (181, 136, 99)
BOARD_BROWN = (240, 217, 181)

CROWN = pygame.transform.scale(pygame.image.load("checkers/assets/crown.png"), (45, 25))
