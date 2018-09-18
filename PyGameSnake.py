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
xmargin = 4
ymargin = 8
margin_color = lightgray
odd_color = white
even_color = black

# game
score = 0


def background_grid():
    global xmargin, ymargin, margin_color, board_width, board_height, square_size, odd_color, even_color
    pygame.draw.rect(DISPLAYSURF, margin_color, (0, 0, board_width * square_size + xmargin * 2, ymargin))  # top margin
    pygame.draw.rect(DISPLAYSURF, margin_color, (0, ymargin, xmargin, board_height * square_size))  # left margin
    pygame.draw.rect(DISPLAYSURF, margin_color, (0, (board_height * square_size + ymargin), board_width * square_size + xmargin * 2, ymargin))  # bottom margin
    pygame.draw.rect(DISPLAYSURF, margin_color, (xmargin + board_width * square_size, ymargin, xmargin, board_height * square_size))  # right margin
    for y in range(board_height):
        for x in range(board_height):
            if (x + y) % 2 == 0:
                draw_square(x, y, even_color)
            else:
                draw_square(x, y, odd_color)
                

def draw_square(x, y, color):
    global square_size, xmargin, ymargin
    pygame.draw.rect(DISPLAYSURF, color, (xmargin + x * square_size, ymargin + y * square_size, square_size, square_size))



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

background_grid()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            key == key_input(event.key)




    pygame.display.update()
    FPSCLOCK.tick(FPS)


