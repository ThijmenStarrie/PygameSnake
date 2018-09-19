import pygame, sys, random
from pygame.locals import *

pygame.init()


# Colors
white      = (255, 255, 255)
black      = (000, 000, 000)
lightgray  = (100, 100, 100)
red        = (232, 72,  29)
green      = (162, 209, 73)
lightgreen = (170, 215, 81)
darkgreen  = (87,  138, 52)

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
xmargin = 10
ymargin = 10
margin_color = darkgreen
odd_color = green
even_color = lightgreen
apple_margin = 4

# game
score = 0
apple_xy = (0, 0)

def background_grid():
    pygame.draw.rect(DISPLAYSURF, margin_color, (0, 0, board_width * square_size + xmargin * 2, ymargin))  # top margin
    pygame.draw.rect(DISPLAYSURF, margin_color, (0, ymargin, xmargin, board_height * square_size))  # left margin
    pygame.draw.rect(DISPLAYSURF, margin_color, (0, (board_height * square_size + ymargin),
                                                 board_width * square_size + xmargin * 2, ymargin))  # bottom margin
    pygame.draw.rect(DISPLAYSURF, margin_color, (xmargin + board_width * square_size, ymargin,
                                                 xmargin, board_height * square_size))  # right margin
    for y in range(board_height):
        for x in range(board_height):
            if (x + y) % 2 == 0:
                draw_square(x, y, even_color)
            else:
                draw_square(x, y, odd_color)
                

def draw_square(x, y, color):
    global square_size, xmargin, ymargin
    pygame.draw.rect(DISPLAYSURF, color, (xmargin + x * square_size, ymargin + y * square_size,
                                          square_size, square_size))

def random_apple():
    apple = (random.randrange(board_width), random.randrange(board_height))
    applex, appley = apple
    pygame.draw.rect(DISPLAYSURF, red, (xmargin + applex * square_size + apple_margin,
                                        ymargin + appley * square_size + apple_margin,
                                        square_size - 2 * apple_margin, square_size - 2 * apple_margin))
    return apple


def key_input(keyinput):
    if keyinput == keyup:
        return "UP"
    if keyinput == keydown:
        return "DOWN"
    if keyinput == keyleft:
        return "LEFT"
    if keyinput == keyright:
        return  "RIGHT"


DISPLAYSURF = pygame.display.set_mode((board_width * square_size + xmargin * 2,
                                       board_height * square_size + ymargin * 2))
pygame.display.set_caption("Snake  - score: " + str(score))

background_grid()
print(random_apple())

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            key == key_input(event.key)





    pygame.display.update()
    FPSCLOCK.tick(FPS)


