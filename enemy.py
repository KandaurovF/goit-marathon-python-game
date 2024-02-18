import pygame
import random
from const import WIDTH, HEIGHT, COLOR_BLUE, ENEMY_SIZE


class Enemy:
    def __init__(self, initial_speed):
        self.surface = pygame.image.load(
            'img/enemy.png')  # pygame.Surface(ENEMY_SIZE)
        # self.surface.fill(COLOR_BLUE)
        self.rect = self.surface.get_rect(
            midleft=(WIDTH, random.randint(ENEMY_SIZE[1] // 2, HEIGHT - ENEMY_SIZE[1] // 2)))
        self.speed = initial_speed

    def move(self):
        self.rect.x -= self.speed

    def is_offscreen(self):
        return self.rect.right < 0


def create_enemy():
    initial_speed = random.randint(2, 4)
    enemy = Enemy(initial_speed)
    return enemy
