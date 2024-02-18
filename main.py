import pygame
import random
from pygame.constants import QUIT
from const import WIDTH, HEIGHT, COLOR_BLACK, COLOR_WHITE, ENEMY_SPAWN_PROBABILITY, BONUS_SPAWN_PROBABILITY
from player import Player
from controls import move_direction
from enemy import create_enemy
from bonuses import create_bonus


pygame.init()

FPS = pygame.time.Clock()

FONT = pygame.font.SysFont('Verdana', 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load(
    'img/background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 1

player = Player((20, 20), (WIDTH // 2, HEIGHT // 2))

enemies = []
bonuses = []
score = 0

playing = True


def game_over():
    global playing
    playing = False


def handle_bonus(bonus):
    global score
    score += 1
    bonuses.remove(bonus)


def update_objects():
    for enemy in enemies:
        enemy.move()
        if enemy.is_offscreen():
            enemies.remove(enemy)
        if pygame.sprite.collide_rect(player, enemy):
            game_over()

    for bonus in bonuses:
        bonus.move()
        if bonus.is_offscreen():
            bonuses.remove(bonus)
        if pygame.sprite.collide_rect(player, bonus):
            handle_bonus(bonus)


def draw_objects():
    # main_display.fill(COLOR_BLACK)
    global bg_X1, bg_X2
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    for enemy in enemies:
        main_display.blit(enemy.surface, enemy.rect)

    for bonus in bonuses:
        main_display.blit(bonus.surface, bonus.rect)

    main_display.blit(player.surface, player.rect)

    main_display.blit(FONT.render(str(score), True,
                      COLOR_WHITE), (WIDTH-50, 20))

    pygame.display.flip()


while playing:
    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    if random.randint(1, 300) <= ENEMY_SPAWN_PROBABILITY:
        new_enemy = create_enemy()
        enemies.append(new_enemy)

    if random.randint(1, 500) <= BONUS_SPAWN_PROBABILITY:
        new_bonus = create_bonus()
        bonuses.append(new_bonus)

    move_direction(player)
    update_objects()
    draw_objects()
