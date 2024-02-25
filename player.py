import pygame
import os
from const import WIDTH, HEIGHT, COLOR_WHITE

IMAGE_PATH = 'img/goose'
PLAYER_IMAGES = os.listdir(IMAGE_PATH)


class Player:
    # def __init__(self, size, initial_position):
    def __init__(self, initial_position):
        self.images = [pygame.image.load(os.path.join(
            IMAGE_PATH, image)).convert_alpha() for image in PLAYER_IMAGES]
        self.surface = self.images[0]  # pygame.Surface(size)
        self.image_index = 0
        self.rect = self.surface.get_rect(center=initial_position)
        self.speed = 6

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

    def change_image(self):
        self.image_index += 1
        if self.image_index >= len(self.images):
            self.image_index = 0
        self.surface = self.images[self.image_index]


def create_player():
    initial_position = (WIDTH // 2, HEIGHT // 2)
    player = Player(initial_position)
    return player
