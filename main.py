import pygame
from time import sleep
from random import randint

pygame.init()

screen = pygame.display.set_mode((1200, 800))

position = [580, 380]
speed = 4

obstacles = []

counter = 0

score = 0

paused = False

font = pygame.font.SysFont('Garamond', 300)

while True:
    pygame.time.Clock().tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
            if event.key == pygame.K_q:
                pygame.quit()
    
    ## Controls
    keyPress = pygame.key.get_pressed()

    motion = [0, 0]

    if keyPress[pygame.K_w] and not position[1] <=0 and paused == False:
        motion[1] -= 1
    elif keyPress[pygame.K_s] and not position[1] >=780 and paused == False:
        motion[1] += 1

    if keyPress[pygame.K_d] and not position[0] >=1180 and paused == False:
        motion[0] += 1
    elif keyPress[pygame.K_a] and not position[0] <=0 and paused == False:
        motion[0] -= 1
    
    if motion[0] != 0 and motion[1] != 0:
        motion[0] = motion[0]/1.5
        motion[1] = motion[1]/1.5

    position[0] += motion[0]*speed
    position[1] += motion[1]*speed
    
    screen.fill((255, 255, 255))
    
    ## Score
    textsurface = font.render(str(score), False, (200, 200, 200))
    screen.blit(textsurface,(525, 300))
    
    ## The player
    player = pygame.draw.rect(screen, (120, 200, 50), (position[0], position[1], 20, 20))

    ## obstacles
    if paused == False:
        counter += 1
    if counter == 100:
        combination = randint(1, 5)
        if combination == 1:
            obstacles.append([0, 100, 30, 400, "right"])
            obstacles.append([0, 600, 30, 200, "right"])
        elif combination == 2:
            obstacles.append([350, 0, 500, 30, "down"])
            obstacles.append([700, 800, 400, 30, "up"])
        elif combination == 3:
            obstacles.append([0, 100, 30, 600, "right"])
            obstacles.append([1200, 300, 30, 300, "left"])
        elif combination == 4:
            obstacles.append([0, 500, 30, 300, "right"])
            obstacles.append([800, 0, 400, 30, "down"])
        elif combination == 5:
            obstacles.append([1200, 500, 30, 300, "left"])
            obstacles.append([200, 795, 400, 30, "up"])
            obstacles.append([0, 100, 30, 300, "right"])

        score += 1
        counter = 0
      
    for value in obstacles:
        rect = pygame.draw.rect(screen, (200, 50, 50), (value[0], value[1], value[2], value[3]))
                
        if value[4] == "right" and paused == False:
            if value[0] >1200:
                obstacles.remove(value)
            else:
                value[0] += 4
        elif value[4] == "left" and paused == False:
            if value[0] <0:
                obstacles.remove(value)
            else:
                value[0] -= 4
        elif value[4] == "up" and paused == False:
            if value[1] <0:
                obstacles.remove(value)
            else:
                value[1] -= 4
        elif value[4] == "down" and paused == False:
            if value[1] >800:
                obstacles.remove(value)
            else:
                value[1] += 4
        if rect.colliderect(player):
            position = [580, 380]
            obstacles = []
            score = 0
    
    if paused == True:
        pygame.draw.rect(screen, (237, 245, 239), (0, 250, 1200, 300))
        textsureface = font.render("Paused", False, (0, 0, 0))
        screen.blit(textsureface, (250, 300))
    
    pygame.display.update()
