def check_for_reset(stats, ball, paddles, scoreboard):
    if ball.rect.left > ball.screen_rect.right:
        # If the ball goes off the the player's right side
        stats.enemy_score += 1
        reset_objects(stats, scoreboard, ball, paddles)

    elif ball.rect.right < ball.screen_rect.left:
        # If the ball goes off the enemy's left side
        stats.player_score += 1
        reset_objects(stats, scoreboard, ball, paddles)

    elif ball.rect.bottom < ball.screen_rect.top or ball.rect.top > ball.screen_rect.bottom:
        # If the ball goes off the top or bottom of the player's side
        if ball.rect.centerx > ball.screen_rect.centerx:
            stats.enemy_score += 1
            reset_objects(stats, scoreboard, ball, paddles)

        # If the ball goes off the top or bottom side of the enemy's side
        else:
            stats.player_score += 1
            reset_objects(stats, scoreboard, ball, paddles)


def reset_objects(stats, scoreboard, ball, paddles):
    scoreboard.prep_scores()
    ball.reset()
    for paddle in paddles:
        paddle.reset()
    if stats.player_score >= 3 or stats.enemy_score >= 3:
        stats.game_active = False
