import pygame
from pygame.sprite import Group
import player_inputs
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ball import Ball
from player_paddle import PlayerPaddle
from enemy_paddle import EnemyPaddle


'''
TO-DO:
-Add difficulty options
'''


def run_game():
    # Initialize pygame, settings, and screen object
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    stats = GameStats()
    scoreboard = Scoreboard(settings, screen, stats)
    button = Button(screen, "Play")

    pygame.display.set_caption("Pong")

    ball = Ball(screen, settings)

    ppt = PlayerPaddle(screen, settings, 1, 0)
    ppb = PlayerPaddle(screen, settings, 1, 1)
    ppr = PlayerPaddle(screen, settings, 0, 2)

    ept = EnemyPaddle(screen, settings, 1, 0)
    epb = EnemyPaddle(screen, settings, 1, 1)
    epr = EnemyPaddle(screen, settings, 0, 2)

    player_paddles = Group()
    player_paddles.add(ppt)
    player_paddles.add(ppb)
    player_paddles.add(ppr)

    enemy_paddles = Group()
    enemy_paddles.add(ept)
    enemy_paddles.add(epb)
    enemy_paddles.add(epr)

    all_paddles = Group()
    all_paddles.add(ppt)
    all_paddles.add(ppb)
    all_paddles.add(ppr)
    all_paddles.add(ept)
    all_paddles.add(epb)
    all_paddles.add(epr)

    while True:
        screen.fill(settings.bg_color)

        player_inputs.check_events(stats, scoreboard, button, player_paddles)
        draw_all_things(ball, all_paddles)
        scoreboard.show_score()
        if not stats.game_active:
            button.draw_button()

        if stats.game_active:
            update_all_things(ball, all_paddles, player_paddles, enemy_paddles)
            gf.check_for_reset(stats, ball, all_paddles, scoreboard)

        pygame.display.flip()


def update_all_things(ball, all_paddles, player_paddles, enemy_paddles):
    ball.update(all_paddles)
    for paddle in player_paddles:
        paddle.update()
    for paddle in enemy_paddles:
        paddle.update(ball)


def draw_all_things(ball, all_paddles):
    ball.draw()
    for paddle in all_paddles:
        paddle.draw()


run_game()
