import pygame
import random
import math

# Initializes pygames
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
running = True

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerimg = pygame.image.load("player.png")
enemy1img = pygame.image.load("enemy1.png")
background = pygame.image.load("background.png")
bulletimg = pygame.image.load("bullet.png")

#Random Enemy Spawn
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)

#50 50 for enemy to start moving left or right
startdir = random.randint(0, 1)

#Bullet location
bulletY = 480
bulletX = 0

#Player Location
playerX = 370
playerY = 480

#Player change values
playerX_change = 0
playerY_change = 0

enemyX_change = 5
score = 0
enemyY_change = enemyY

#Bullet Movement
bulletX_change = 0
bulletY_change = 10
# ready = not shot, fire = moving
bullet_state = "ready"

if startdir:
    enemyX_change = -5
r = 0
g = 0
b = 0


#Player function to display player
def player(x, y):
    screen.blit(playerimg, (x, y))


#Player function to display enemy
def enemy(x, y):
    screen.blit(enemy1img, (x, y))

#Bullet function to fire bullet
def firebullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

#Uses distance formula for collision detection between bullet and enemy
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
while running:
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

    enemyX += enemyX_change
    if enemyX >= 736:
        enemyX_change = -5
        enemyY += 60
    if enemyX <= 0:
        enemyX_change = 5
        enemyY += 60

    # RGB screen fill
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    # Bullet Fire
    if bullet_state is "fire":
        firebullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bullet_state = "ready"
            bulletY = 480

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
