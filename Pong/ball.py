import pygame
import random
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, screen, settings):
        # self.image = pygame.image.load('images/paddle.png')
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(0, 0, settings.ball_size, settings.ball_size)
        self.rect.center = self.screen_rect.center

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.ball_start_speed = settings.ball_start_speed
        self.ball_acceleration = settings.ball_acceleration
        self.ball_angular_influence = settings.ball_angular_influence
        self.ball_sound = pygame.mixer.Sound('sounds/blip.wav')

        rand_vel = random.uniform(-self.ball_start_speed, self.ball_start_speed)
        self.velocity_x = rand_vel
        self.velocity_y = self.ball_start_speed - abs(rand_vel)

        self.last_paddle_collided_with = None

    def update(self, paddles):
        self.velocity_x += self.ball_acceleration if self.velocity_x > 0 else -self.ball_acceleration
        self.center_x += self.velocity_x
        self.rect.centerx = self.center_x

        collision = pygame.sprite.spritecollideany(self, paddles)
        self.calculate_horizontal_collision(collision)

        self.velocity_y += self.ball_acceleration if self.velocity_y > 0 else -self.ball_acceleration
        self.center_y += self.velocity_y
        self.rect.centery = self.center_y

        collision = pygame.sprite.spritecollideany(self, paddles)
        self.calculate_vertical_collision(collision)

    def calculate_horizontal_collision(self, collision):
        if collision:
            if collision != self.last_paddle_collided_with:
                self.last_paddle_collided_with = collision
                self.velocity_x *= -1
                difference = self.rect.centery - collision.rect.centery
                velocity_change_amount = difference * self.ball_angular_influence
                self.velocity_y += velocity_change_amount
                self.ball_sound.play()

    def calculate_vertical_collision(self, collision):
        if collision:
            if collision != self.last_paddle_collided_with:
                self.last_paddle_collided_with = collision
                self.velocity_y *= -1
                difference = self.rect.centerx - collision.rect.centerx
                velocity_change_amount = difference * self.ball_angular_influence
                self.velocity_x += velocity_change_amount
                self.ball_sound.play()

    def draw(self):
        # pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
        pygame.draw.circle(self.screen, (255, 255, 255), self.rect.center, self.rect.width)

    def reset(self):
        rand_vel = random.uniform(-self.ball_start_speed, self.ball_start_speed)
        self.velocity_x = rand_vel
        self.velocity_y = self.ball_start_speed - rand_vel
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.centery
        self.last_paddle_collided_with = None
