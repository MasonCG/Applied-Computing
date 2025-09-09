# this is an example of procedural programming


import pygame

# initializing pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 600))

ballx = 400
bally = 300
ballSize = 15
balldx = 10
balldy = 10

while True:

    # clearing screen
    screen.fill((0, 0, 0))

    # getting event key bumps
    pygame.event.pump()
    # getting keys that are pressed
    keys = pygame.key.get_pressed()
    # end program if escape key is pressed
    if keys[pygame.K_ESCAPE]:
        break

    ballx += balldx
    bally += balldy

    if ballx - ballSize < 0:
        balldx = - balldx
    if ballx + ballSize > screen.get_width():
        balldx = - balldx
    if bally - ballSize < 0:
        balldy = - balldy
    if bally + ballSize > screen.get_height():
        balldy = - balldy

    pygame.draw.circle(screen, (255, 0, 0), (ballx, bally), ballSize)

    pygame.display.update()

pygame.QUIT()




