import pygame
import random
import math

# Initializes pygames
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
running = True

numenemies = 6
enemy1img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemyimage = pygame.image.load("enemy1.png")
for i in range(numenemies):
    enemy1img.append(enemyimage)
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    startdir = random.randint(0, 1)
    if startdir:
        enemyX_change.append(-4)
    else:
        enemyX_change.append(4)
    enemyY_change.append(40)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerimg = pygame.image.load("player.png")
background = pygame.image.load("background.png")
bulletimg = pygame.image.load("bullet.png")

# 50 50 for enemy to start moving left or right

# Bullet location
bulletY = 480
bulletX = 0

# Player Location
playerX = 370
playerY = 480

# Player change values
playerX_change = 0
playerY_change = 0

# Bullet Movement
bulletX_change = 0
bulletY_change = 10
# ready = not shot, fire = moving
bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score,(textX,textY))
# Player function to display player
def player(x, y):
    screen.blit(playerimg, (x, y))


# Player function to display enemy
def enemy(x, y, i):
    screen.blit(enemy1img[i], (x, y))


# Bullet function to fire bullet
def firebullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


# Uses distance formula for collision detection between bullet and enemy
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # move based on keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE and bullet_state is "ready":
                firebullet(playerX, bulletY)
                bulletX = playerX
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX >= 736:
        playerX = 736
    if playerX <= 0:
        playerX = 0

    for i in range(numenemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += 60
        elif enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += 60

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # background image

    # Bullet Fire
    if bullet_state is "fire":
        firebullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bullet_state = "ready"
            bulletY = 480

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
