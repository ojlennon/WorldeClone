import pygame, sys
from pygame.locals import *
 
pygame.init()
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
width = 400
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hello World!')

while True: # main game loop
	screen.fill(BLACK)
	x, y = pygame.mouse.get_pos()
	pygame.draw.line(RED, (x,0), (x,height))

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

    pygame.display.update()
