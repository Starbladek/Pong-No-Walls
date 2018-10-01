class Settings:

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 128)

        # Paddle settings
        self.paddle_length = 150
        self.paddle_thickness = 15
        self.paddle_speed = 2.5

        self.enemy_paddle_length = 150
        self.enemy_paddle_thickness = 15
        self.enemy_paddle_speed = 2
        self.enemy_paddle_speed_degradation = 0.0002    # How much slower the enemy paddles get every frame

        # Ball settings
        self.ball_size = 15
        self.ball_start_speed = 1
        self.ball_acceleration = 0.000015   # How much faster the ball gets every frame
        self.ball_angular_influence = 0.01  # How much the velocity is changed when the ball is hit at an angle

        # Enemy settings
        self.enemy_speed = 0.01             # How quickly the enemy will reach the ball's centerx
