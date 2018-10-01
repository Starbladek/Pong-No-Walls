import pygame.font


class Scoreboard:

    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.font = pygame.font.SysFont(None, 48)

        self.player_score_image = None
        self.player_score_rect = None
        self.enemy_score_image = None
        self.enemy_score_rect = None

        self.prep_scores()

    def prep_scores(self):
        rounded_player_score = int(round(self.stats.player_score, 1))
        score_str = "{:,}".format(rounded_player_score)
        self.player_score_image = self.font.render(score_str, True, (0, 255, 0), self.settings.bg_color)
        self.player_score_rect = self.player_score_image.get_rect()
        self.player_score_rect.right = self.screen_rect.right - 20
        self.player_score_rect.top = 20

        rounded_enemy_score = int(round(self.stats.enemy_score, 1))
        score_str = "{:,}".format(rounded_enemy_score)
        self.enemy_score_image = self.font.render(score_str, True, (255, 0, 0), self.settings.bg_color)
        self.enemy_score_rect = self.enemy_score_image.get_rect()
        self.enemy_score_rect.left = self.screen_rect.left + 20
        self.enemy_score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.player_score_image, self.player_score_rect)
        self.screen.blit(self.enemy_score_image, self.enemy_score_rect)
