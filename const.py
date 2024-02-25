import pygame

pygame.init()

SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH = SCREEN.get_width()
HEIGHT = SCREEN.get_height()
pygame.mouse.set_visible(False)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)

ENEMY_SPAWN_PROBABILITY = 3
BONUS_SPAWN_PROBABILITY = 5
