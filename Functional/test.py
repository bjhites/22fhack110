import sys, pygame
from player import Player

pygame.init()

size = width, height = 640, 480
speed = [1, 1]
green = 55, 255, 110

screen = pygame.display.set_mode(size)
player = Player(1, pygame.Rect(15, 15, 15 ,15))
ballrect = player.getRect()
clock = pygame.time.Clock()
while 1:
    # Sets frame rate
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            player.getKeyDown(event)
        if event.type == pygame.KEYUP:
            player.getKeyUp(event)
        if event.type == pygame.QUIT: sys.exit()

    player.move()

    screen.fill(green)
    pygame.draw.rect(screen, (0,0,0), ballrect)
    pygame.display.flip()