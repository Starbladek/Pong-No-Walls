import pygame
from pygame.sprite import Sprite


class EnemyPaddle(Sprite):

    def __init__(self, screen, settings, direction, side):
        # self.image = pygame.image.load('images/paddle.png')
        super(EnemyPaddle, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.enemy_paddle_max_speed = settings.enemy_paddle_speed
        self.enemy_paddle_speed = settings.enemy_paddle_speed
        self.enemy_paddle_speed_degradation = settings.enemy_paddle_speed_degradation
        self.direction = direction  # 0 = vertical, 1 = horizontal
        self.side = side            # 0 = top, 1 = bottom, 2 = left

        if direction == 0:
            self.rect = pygame.Rect(0, 0, settings.paddle_thickness, settings.paddle_length)
        else:
            self.rect = pygame.Rect(0, 0, settings.paddle_length, settings.paddle_thickness)

        if side == 0:
            self.rect.centerx = self.screen_rect.centerx * 0.5
            self.rect.top = self.screen_rect.top
        elif side == 1:
            self.rect.centerx = self.screen_rect.centerx * 0.5
            self.rect.bottom = self.screen_rect.bottom
        elif side == 2:
            self.rect.left = self.screen_rect.left
            self.rect.centery = self.screen_rect.centery

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

    def update(self, ball):
        # Vertical paddles
        if self.direction == 0:
            if ball.rect.centery > self.center_y and self.rect.bottom < self.screen_rect.bottom:
                self.center_y += self.enemy_paddle_speed
            elif ball.rect.centery < self.center_y and self.rect.top > self.screen_rect.top:
                self.center_y -= self.enemy_paddle_speed

        # Horizontal paddles
        elif self.direction == 1:
            if ball.rect.centerx > self.center_x and self.rect.right < self.screen_rect.centerx:
                self.center_x += self.enemy_paddle_speed
            elif ball.rect.centerx < self.center_x and self.rect.left > self.screen_rect.left:
                self.center_x -= self.enemy_paddle_speed

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

        if self.enemy_paddle_speed > 0.1:
            self.enemy_paddle_speed -= self.enemy_paddle_speed_degradation
        else:
            self.enemy_paddle_speed = 0.1

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def reset(self):
        if self.side == 0:
            self.rect.centerx = self.screen_rect.centerx * 0.5
            self.rect.top = self.screen_rect.top
        elif self.side == 1:
            self.rect.centerx = self.screen_rect.centerx * 0.5
            self.rect.bottom = self.screen_rect.bottom
        elif self.side == 2:
            self.rect.left = self.screen_rect.left
            self.rect.centery = self.screen_rect.centery

        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
        self.enemy_paddle_speed = self.enemy_paddle_max_speed
