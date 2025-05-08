
import pygame
import random
# initialize
pygame.init()
# font 
title_font = pygame.font.SysFont("couriernew", 60)
# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

# Load background images
background_image = pygame.image.load("OIP.jpg")
background_image = pygame.transform.scale(background_image, (800, 600))

menu_background = pygame.image.load("OIP.jpg")
menu_background = pygame.transform.scale(menu_background, (800, 600))

game_over_background = pygame.image.load("OIP.jpg")
game_over_background = pygame.transform.scale(game_over_background, (800, 600))

# Load heart image
heart_image = pygame.image.load("heart.png")
heart_image = pygame.transform.scale(heart_image, (30, 30))

# Paddle variables
paddle_x = 350
paddle_y = 550
paddle_width = 100
paddle_height = 20
paddle_speed = 10

# Ball variables
balls = [{"x": 400, "y": 530, "dx": 4, "dy": -4, "active": False}]
radius = 10

# Extra life variables
falling_hearts = []

# Blocks setup
block_types = {
    "gold": {"color": (255, 215, 0), "hits": 4},
    "silver": {"color": (192, 192, 192), "hits": 3},
    "bronze": {"color": (205, 127, 50), "hits": 2}
}

block_rows = 5
block_cols = 11
block_width = 67
block_height = 20

# Create blocks
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block_x = 10 + col * (block_width + 5)
        block_y = 10 + row * (block_height + 10)
        if row < 2:
            block_type = "gold"
        elif row < 4:
            block_type = "silver"
        else:
            block_type = "bronze"
        blocks.append({
            "rect": pygame.Rect(block_x, block_y, block_width, block_height),
            "type": block_type,
            "hits_left": block_types[block_type]["hits"]
        })

# Game variables
score = 0
lives = 3
high_score = 0
font = pygame.font.Font(None, 36)

# Colors
ball_color = (173, 216, 230)
paddle_color = (0, 255, 0)
text_color = (255, 255, 255)
background_color = (0, 0, 0)

# High Score File
def read_high_score():
    global high_score
    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read())
    except:
        high_score = 0

def write_high_score():
    with open("high_score.txt", "w") as f:
        f.write(str(high_score))

# Function to reset the ball
def reset_ball(ball):
    ball["x"] = paddle_x + paddle_width // 2
    ball["y"] = paddle_y - radius
    ball["dx"] = random.choice([-4, 4])
    ball["dy"] = -4
    ball["active"] = False

# Game Over screen
def show_game_over():
    global high_score
    if score > high_score:
        high_score = score
        write_high_score()

    game_over_running = True
    while game_over_running:
        screen.fill(background_color)
        screen.blit(game_over_background, (0, 0))
        title_font = pygame.font.Font(None, 72)
        text_font = pygame.font.Font(None, 48)

        title = title_font.render("Game Over", True, (255, 0, 0))
        score_display = text_font.render(f"Your Score: {score}", True, text_color)
        high_score_display = text_font.render(f"High Score: {high_score}", True, text_color)
        restart_message = text_font.render("Press R to Restart", True, text_color)
        quit_message = text_font.render("Press Q to Quit", True, text_color)
        menu_message = text_font.render("Press M for Main Menu", True, text_color)

        screen.blit(title, (250, 180))
        screen.blit(score_display, (250, 260))
        screen.blit(high_score_display, (250, 310))
        screen.blit(restart_message, (220, 360))
        screen.blit(quit_message, (220, 410))
        screen.blit(menu_message, (220, 460))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop()
                    game_over_running = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_m:
                    main_menu()
                    game_over_running = False

# Main Menu
def main_menu():
    read_high_score()
    menu_running = True
    while menu_running:
        screen.fill(background_color)
        screen.blit(menu_background, (0, 0))
        title_font = pygame.font.Font(None, 72)
        menu_font = pygame.font.Font(None, 48)

        title = title_font.render("Breakout Game", True,(255,0,0))
        start_option = menu_font.render("1. Start the Game", True, text_color)
        high_score_option = menu_font.render("2. High Score", True, text_color)
        quit_option = menu_font.render("3. Quit", True, text_color)

        screen.blit(title, (250, 150))
        screen.blit(start_option, (250, 250))
        screen.blit(high_score_option, (250, 300))
        screen.blit(quit_option, (250, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    menu_running = False
                    game_loop()
                elif event.key == pygame.K_2:
                    show_high_score()
                elif event.key == pygame.K_3:
                    pygame.quit()
                    exit()

# Show high score
def show_high_score():
    high_score_running = True
    while high_score_running:
        screen.fill(background_color)
        title_font = pygame.font.Font(None, 72)
        high_score_font = pygame.font.Font(None, 48)

        title = title_font.render("High Score", True, text_color)
        high_score_display = high_score_font.render(f"High Score: {high_score}", True, text_color)
        back_message = high_score_font.render("Press B to go back", True, text_color)

        screen.blit(title, (250, 150))
        screen.blit(high_score_display, (250, 250))
        screen.blit(back_message, (250, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    high_score_running = False
                    main_menu()

# Pause Menu
def show_pause_menu():
    global paused
    pause_running = True
    while pause_running:
        screen.fill(background_color)
        title_font = pygame.font.Font(None, 72)
        menu_font = pygame.font.Font(None, 48)

        title = title_font.render("Game Paused", True, text_color)
        resume_option = menu_font.render("Press R to Resume", True, text_color)
        quit_option = menu_font.render("Press Q to Quit", True, text_color)

        screen.blit(title, (250, 150))
        screen.blit(resume_option, (250, 250))
        screen.blit(quit_option, (250, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    paused = False
                    pause_running = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# Game Loop
def game_loop():
    global score, lives, balls, blocks, paddle_x, paddle_y, ball_on_paddle, paused, falling_hearts
    score = 0
    lives = 3
    ball_on_paddle = True
    paused = False
    falling_hearts = []

    for ball in balls:
        reset_ball(ball)

    blocks.clear()
    for row in range(block_rows):
        for col in range(block_cols):
            block_x = 10 + col * (block_width + 5)
            block_y = 10 + row * (block_height + 10)
            if row < 2:
                block_type = "gold"
            elif row < 4:
                block_type = "silver"
            else:
                block_type = "bronze"
            blocks.append({
                "rect": pygame.Rect(block_x, block_y, block_width, block_height),
                "type": block_type,
                "hits_left": block_types[block_type]["hits"]
            })

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and ball_on_paddle:
                    for ball in balls:
                        ball["active"] = True
                    ball_on_paddle = False
                elif event.key == pygame.K_ESCAPE:
                    paused = True
                    show_pause_menu()

        if paused:
            continue

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < 800 - paddle_width:
            paddle_x += paddle_speed

        for ball in balls:
            if ball_on_paddle:
                ball["x"] = paddle_x + paddle_width // 2
                ball["y"] = paddle_y - radius
            else:
                ball["x"] += ball["dx"]
                ball["y"] += ball["dy"]

                if ball["x"] - radius < 0 or ball["x"] + radius > 800:
                    ball["dx"] = -ball["dx"]
                if ball["y"] - radius < 0:
                    ball["dy"] = -ball["dy"]

                if paddle_y < ball["y"] + radius < paddle_y + paddle_height and paddle_x < ball["x"] < paddle_x + paddle_width:
                    ball["dy"] = -ball["dy"]

                if ball["y"] - radius > 600:
                    lives -= 1
                    ball_on_paddle = True
                    reset_ball(ball)
                    if lives == 0:
                        show_game_over()

                ball_rect = pygame.Rect(ball["x"] - radius, ball["y"] - radius, radius * 2, radius * 2)
                for block in blocks[:]:
                    if block["rect"].colliderect(ball_rect):
                        block["hits_left"] -= 1
                        ball["dy"] = -ball["dy"]
                        score += 1
                        if block["hits_left"] == 0:
                            blocks.remove(block)
                            if random.random() < 0.3:  # 30% chance to drop heart
                                heart_x = block["rect"].x + block_width // 2 - 15
                                heart_y = block["rect"].y
                                falling_hearts.append({"x": heart_x, "y": heart_y})
                        break

        # Move hearts
        for heart in falling_hearts[:]:
            heart["y"] += 5
            if paddle_y < heart["y"] + 30 < paddle_y + paddle_height and paddle_x < heart["x"] < paddle_x + paddle_width:
                lives += 1
                falling_hearts.remove(heart)
            elif heart["y"] > 600:
                falling_hearts.remove(heart)

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, paddle_color, (paddle_x, paddle_y, paddle_width, paddle_height))

        for block in blocks:
            color = block_types[block["type"]]["color"]
            adjusted_color = tuple(c * block["hits_left"] // block_types[block["type"]]["hits"] for c in color)
            pygame.draw.rect(screen, adjusted_color, block["rect"])

        for ball in balls:
            pygame.draw.circle(screen, ball_color, (int(ball["x"]), int(ball["y"])), radius)

        for heart in falling_hearts:
            screen.blit(heart_image, (heart["x"], heart["y"]))

        score_text = font.render(f"Score: {score}", True, (255, 0, 0))
        lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))

        pygame.display.flip()
        clock.tick(60)

# Start Game
main_menu()
pygame.quit()


