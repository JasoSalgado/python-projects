"""
UFO INVASION
"""
# modules
import pygame
import random
import math
from pygame import mixer

# Iniciate pygame
pygame.init()

# Screen size
screen = pygame.display.set_mode((800, 600))

# Title and icon config
pygame.display.set_caption('UFO Invasion')
icon = pygame.image.load('ovni.png')
pygame.display.set_icon(icon)
background_img = pygame.image.load('fondo.jpeg')

# Music
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Player variables
player_img = pygame.image.load('cohete.png')
player_x = 368
player_y = 500
player_x_change = 0

# UFO variables
# We can create the same using a Class method
ufo_img = []
ufo_x = []
ufo_y = []
ufo_x_change = []
ufo_y_change = []
ufo_amount = 8

for u in range(ufo_amount):
    # UFO variables
    ufo_img.append(pygame.image.load('enemigo.png'))
    ufo_x.append(random.randint(0, 736))
    ufo_y.append(random.randint(50, 200))
    ufo_x_change.append(1)
    ufo_y_change.append(50)

# Bullet variables
bullet_img = pygame.image.load('bala.png')
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 3
bullet_visible = False

# Score variables
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
coordinate_x = 10
coordinate_y = 10

# End game
final_font = pygame.font.Font('freesansbold.ttf', 40)

def end_game():
    """
    End game
    """
    my_final_font = final_font.render('GAME OVER!', True, (255, 255, 255))
    screen.blit(my_final_font, (60, 200))


def display_score(x, y):
    """
    Display score on the screen
    """
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (x, y))


def player(x, y):
    """
    Player event
    """
    screen.blit(player_img, (x, y))


def ufo(x, y, enemy):
    """
    UFO event
    """
    screen.blit(ufo_img[enemy], (x, y))


def shot_bullet(x, y):
    """
    Shot bullet
    """
    global bullet_visible 
    bullet_visible = True
    screen.blit(bullet_img, (x + 16, y + 10))


def collision(x_1, y_1, x_2, y_2):
    """
    Detect collisions between UFO and bullet
    """
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distance < 27:
        return True
    else:
        return False


# QUIT event to close the window
executes = True

while executes:
    # Background image
    # It is necessary to update the screen
    screen.blit(background_img, (0, 0))

    # Iterate events
    for event in pygame.event.get():

        # Close event
        if event.type == pygame.QUIT:
            executes = False
        
        # Left, right movement with key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            # Key space
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('disparo.mp3')
                bullet_sound.play()
                if bullet_visible == False:
                   bullet_x = player_x
                   shot_bullet(bullet_x, bullet_y)

        # Release keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Modify player´s location
    player_x += player_x_change

    # Player´s border limit
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    
    # Modify ufo´s location
    for e in range(ufo_amount):
        # End game
        if ufo_y[e] > 500:
            for k in range(ufo_amount):
                ufo_y[k] == 1000 # To hide ufos
            end_game()
            break

        ufo_x[e] += ufo_x_change[e]
    
        # Ufo´s border limit
        if ufo_x[e] <= 0:
            ufo_x_change[e] = 1
            ufo_y[e] += ufo_y_change[e]
        elif ufo_x[e] >= 736:
            ufo_x_change[e] = -1
            ufo_y[e] += ufo_y_change[e]
        
         # Colission
        there_is_collision = collision(ufo_x[e], ufo_y[e], bullet_x, bullet_y)
        if there_is_collision:
            collision_sound = mixer.Sound('golpe.mp3')
            collision_sound.play()
            bullet_y = 500
            bullet_visible = False
            score += 1
            ufo_x[e] = random.randint(0, 736)
            ufo_y[e] = random.randint(50, 200)
        
        ufo(ufo_x[e], ufo_y[e], e)
    
    # Bullet movement
    if bullet_y == -64: # Bullet size is 64
        bullet_y = 500
        bullet_visible = False

    if bullet_visible:
        shot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    display_score(coordinate_x, coordinate_y)

    # Update
    pygame.display.update()