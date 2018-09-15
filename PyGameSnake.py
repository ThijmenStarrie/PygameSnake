import pygame, sys, random
from pygame.locals import *

pygame.init()


# Colors
white     = (255, 255, 255)
black     = (000, 000, 000)
lightgray = (100, 100, 100)

# Keys
keyup = 273
keyleft = 276
keyright = 275
keydown = 274
key = "none"

# graphics
FPS = 12
FPSCLOCK = pygame.time.Clock()
square_size = 32
board_width = 16
board_height = 16
xmargin = 32
ymargin = 32
margin_color = lightgray
odd_color = white
even_color = black

# game
score = 0


def background_grid(mx, my, mcolor, bwidth, bhight, sqsize, odd, even):
    pygame.draw.rect(DISPLAYSURF, mcolor, (0, 0, bwidth * sqsize + my * 2, my))
    pygame.draw.rect(DISPLAYSURF, mcolor, (0, my, mx, bhight * sqsize))
    pygame.draw.rect(DISPLAYSURF, mcolor, (0, (bhight * sqsize + mx), bwidth * sqsize + my * 2, mx))
    pygame.draw.rect(DISPLAYSURF, mxolor, )



def key_input(keyinput):
    if keyinput == keyup:
        return "UP"
    if keyinput == keydown:
        return "DOWN"
    if keyinput == keyleft:
        return "LEFT"
    if keyinput == keyright:
        return  "RIGHT"


DISPLAYSURF = pygame.display.set_mode((board_width * square_size + xmargin * 2, board_height * square_size + ymargin * 2))
pygame.display.set_caption("Snake  - score: " + str(score))

background_grid(xmargin, ymargin, margin_color, board_width, board_height, square_size, odd_color, even_color)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            key == key_input(event.key)




    pygame.display.update()
    FPSCLOCK.tick(FPS)


