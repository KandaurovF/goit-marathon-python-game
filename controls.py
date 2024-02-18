import pygame
from pygame.constants import K_DOWN, K_UP, K_RIGHT, K_LEFT


def move_direction(player):
    keys = pygame.key.get_pressed()
    if keys[K_DOWN]:
        player.move("DOWN")
    if keys[K_UP]:
        player.move("UP")
    if keys[K_RIGHT]:
        player.move("RIGHT")
    if keys[K_LEFT]:
        player.move("LEFT")
