# this is an example of procedural programming


import pygame
import random

# initializing pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 600))

class Ball(object):
    def __init__(self, x = 400, y = 300, r = 15, dx=1, dy=1, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.color = color

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x + self.r > screen.get_width():
            self.dx *= -1
        if self.x - self.r < 0:
            self.dx *= -1
        if self.y + self.r > screen.get_height():
            self.dy *= -1
        if self.y - self.r < 0:
            self.dy *= -1

    def render(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


def randomColor():
    r = 255
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = [r, g, b]
    random.shuffle(rgb)
    return rgb

balls =[]
for i in range(100):
    ball = Ball(
        x = random.uniform(100, 500),
        y = random.uniform(100, 500),
        r = random.uniform(5, 25),
        dx = random.uniform(-7, 7),
        dy = random.uniform(-7, 7),
        color = randomColor()
    )
    
    balls.append(ball)

clock = pygame.time.Clock()
FPS = 60


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


    for ball in balls:
        ball.move()
        ball.render()
    
    clock.tick(FPS)
    pygame.display.update()

pygame.QUIT()




