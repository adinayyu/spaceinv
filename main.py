import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('spaceinvaders (1).png')
pygame.display.set_icon(icon)

#Player
playerImg= pygame.image.load('spaceship-png-11552939050w6qgx.png')
playerX=370
playerY=480
playerX_change=0

def player(x,y):
    screen.blit(playerImg,(x,y))

#Game loop
running=True
while running:
    #RGB- Red,Green,Blue
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #if keystroke is pressed check whether its right or left
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.3
            if event.key==pygame.K_RIGHT:
                playerX_change=0.3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

    #5=5+-0.1->5=5-0.1
    #5=5+0.1
    playerX+=playerX_change
    player(playerX,playerY)
    pygame.display.update()