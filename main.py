import pygame
import random
from pygame.constants import QUIT
from const import SCREEN, WIDTH, HEIGHT, COLOR_BLACK, ENEMY_SPAWN_PROBABILITY, BONUS_SPAWN_PROBABILITY
from player import create_player
from controls import move_direction
from enemy import create_enemy
from bonuses import create_bonus


pygame.init()

FPS = pygame.time.Clock()

FONT = pygame.font.SysFont('Verdana', 20)


bg = pygame.transform.scale(pygame.image.load(
    'img/background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 4


player = create_player()

CHANGE_IMAGE = pygame.USEREVENT+1
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []
bonuses = []

score = 0

game_over_stat = False


def game_over():
    global game_over_stat
    game_over_stat = True


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
            return
    for bonus in bonuses:
        bonus.move()
        if bonus.is_offscreen():
            bonuses.remove(bonus)
        if pygame.sprite.collide_rect(player, bonus):
            handle_bonus(bonus)


def draw_objects():
    # SCREEN.fill(COLOR_BLACK)
    global bg_X1, bg_X2
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    SCREEN.blit(bg, (bg_X1, 0))
    SCREEN.blit(bg, (bg_X2, 0))

    for enemy in enemies:
        SCREEN.blit(enemy.surface, enemy.rect)

    for bonus in bonuses:
        SCREEN.blit(bonus.surface, bonus.rect)

    SCREEN.blit(player.surface, player.rect)

    SCREEN.blit(FONT.render(str(score), True,
                            COLOR_BLACK), (WIDTH-50, 20))
    SCREEN.blit(FONT.render(str('Press ESC to Exit'),
                True, COLOR_BLACK), (30, HEIGHT-50))

    pygame.display.flip()


while True:
    FPS.tick(80)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        if event.type == CHANGE_IMAGE:
            player.change_image()

    if not game_over_stat:
        if random.randint(1, 200) <= ENEMY_SPAWN_PROBABILITY:
            new_enemy = create_enemy()
            enemies.append(new_enemy)

        if random.randint(1, 500) <= BONUS_SPAWN_PROBABILITY:
            new_bonus = create_bonus()
            bonuses.append(new_bonus)

        move_direction(player)
        update_objects()
        draw_objects()
    else:
        SCREEN.blit(FONT.render("GAME OVER", True, COLOR_BLACK),
                    (WIDTH // 2 - 50, HEIGHT // 2))

        pygame.display.flip()
