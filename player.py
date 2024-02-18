import pygame
from const import WIDTH, HEIGHT, COLOR_WHITE


class Player:
    def __init__(self, size, initial_position):
        self.surface = pygame.image.load(
            'img/player.png').convert_alpha()  # pygame.Surface(size)
        # self.surface.fill(COLOR_WHITE)
        self.rect = self.surface.get_rect(center=initial_position)
        self.speed = 5

    def move(self, direction):
        if direction == "UP":
            self.rect.y -= self.speed
        elif direction == "DOWN":
            self.rect.y += self.speed
        elif direction == "LEFT":
            self.rect.x -= self.speed
        elif direction == "RIGHT":
            self.rect.x += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
