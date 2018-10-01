import pygame
from pygame.sprite import Sprite


class PlayerPaddle(Sprite):

    def __init__(self, screen, settings, direction, side):
        # self.image = pygame.image.load('images/paddle.png')
        super(PlayerPaddle, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.paddle_speed = settings.paddle_speed
        self.direction = direction  # 0 = vertical, 1 = horizontal
        self.side = side            # 0 = top, 1 = bottom, 2 = right

        if direction == 0:
            self.rect = pygame.Rect(0, 0, settings.paddle_thickness, settings.paddle_length)
        else:
            self.rect = pygame.Rect(0, 0, settings.paddle_length, settings.paddle_thickness)

        if side == 0:
            self.rect.centerx = self.screen_rect.centerx * 1.5
            self.rect.top = self.screen_rect.top
        elif side == 1:
            self.rect.centerx = self.screen_rect.centerx * 1.5
            self.rect.bottom = self.screen_rect.bottom
        elif side == 2:
            self.rect.right = self.screen_rect.right
            self.rect.centery = self.screen_rect.centery

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        # Vertical paddles
        if self.direction == 0:
            if self.moving_up and self.rect.y > self.screen_rect.top:
                self.center_y -= self.paddle_speed
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.center_y += self.paddle_speed

        # Horizontal paddles
        elif self.direction == 1:
            if self.moving_left and self.rect.left > self.screen_rect.centerx:
                self.center_x -= self.paddle_speed
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center_x += self.paddle_speed

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect)
        pygame.draw.line(self.screen, (255, 255, 255), [self.screen_rect.centerx, self.screen_rect.top],
                         [self.screen_rect.centerx, self.screen_rect.bottom])

    def reset(self):
        if self.side == 0:
            self.rect.centerx = self.screen_rect.centerx * 1.5
            self.rect.top = self.screen_rect.top
        elif self.side == 1:
            self.rect.centerx = self.screen_rect.centerx * 1.5
            self.rect.bottom = self.screen_rect.bottom
        elif self.side == 2:
            self.rect.right = self.screen_rect.right
            self.rect.centery = self.screen_rect.centery

        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
