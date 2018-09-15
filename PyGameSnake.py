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
square_size = 16
board_width = 16
board_hight = 16
xmargin = 5
ymargin = 5
margin_color = lightgray
odd_color = white
even_color = black


def background_grid(mx, my, mcolor, bwidth, bhight, sqsize, odd, even):
    pygame.draw.rect(DISPLAYSURF, mcolor, (0, 0), (board_width * square_size + xmargin * 2, my))




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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            key == key_input(event.key)




    pygame.display.update()
    FPSCLOCK.tick(FPS)


