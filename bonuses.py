import pygame
import random
from const import WIDTH, HEIGHT, COLOR_YELLOW

BONUS_SIZE = (70, 80)


class Bonus:
    def __init__(self, initial_speed):
        self.surface = pygame.transform.scale(pygame.image.load(
            'img/bonus.png').convert_alpha(), BONUS_SIZE)

        # self.surface.fill(COLOR_YELLOW)
        self.rect = self.surface.get_rect(
            midtop=(random.randint(BONUS_SIZE[0] // 2, WIDTH - BONUS_SIZE[0] // 2), 0))
        self.speed = initial_speed

    def move(self):
        self.rect.y += self.speed

    def is_offscreen(self):
        return self.rect.top > HEIGHT


def create_bonus():
    initial_speed = random.randint(3, 5)
    bonus = Bonus(initial_speed)
    return bonus
