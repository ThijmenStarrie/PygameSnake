import pygame
import sys
import random
from pygame.locals import *

pygame.init()

# Colors
white = (255, 255, 255)
black = (000, 000, 000)
lightgray = (100, 100, 100)
red = (232, 72,  29)
green = (162, 209, 73)
lightgreen = (170, 215, 81)
darkgreen = (87,  138, 52)
blue = (0,   0,   255)
darkblue = (0,   0,   150)


# keys
keyup = 273
keyleft = 276
keyright = 275
keydown = 274
direction = (0, 0)
last_direction = (0, 0)

# graphics
FPS = 8
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
snake_margin = 4
snake_color = blue
snake_head_color = darkblue
apple_color = red


# game
score = 0
apple_xy = (8, 8)
snake_xy = [(2, 8)]
ate_apple = False
dead = False


def background_grid():
    pygame.draw.rect(DISPLAYSURF, margin_color, (0, 0, board_width *
                                                 square_size + xmargin * 2, ymargin))  # top margin
    pygame.draw.rect(DISPLAYSURF, margin_color, (0, ymargin, xmargin,
                                                 board_height * square_size))  # left margin
    pygame.draw.rect(DISPLAYSURF, margin_color, (0, (board_height * square_size
                                                     + ymargin), board_width * square_size +
                                                 xmargin * 2, ymargin))  # bottom margin
    pygame.draw.rect(DISPLAYSURF, margin_color, (xmargin + board_width *
                                                 square_size, ymargin, xmargin, board_height
                                                 * square_size))  # right margin
    for y in range(board_height):
        for x in range(board_height):
            if (x + y) % 2 == 0:
                draw_square(x, y, even_color)
            else:
                draw_square(x, y, odd_color)


def draw_square(x, y, color):
    global square_size, xmargin, ymargin
    pygame.draw.rect(DISPLAYSURF, color, (xmargin + x * square_size,
                                          ymargin + y * square_size, square_size, square_size))


def random_apple():
    retry = False
    while True:
        apple = (random.randrange(board_width), random.randrange(board_height))
        applex, appley = apple
        for s in snake_xy:
            if s == apple:
                retry is True
                break
        else:
            retry is False
        if retry is False:
            break
    pygame.draw.rect(DISPLAYSURF, apple_color, (xmargin + applex * square_size
                                                + apple_margin, ymargin + appley * square_size
                                                + apple_margin, square_size - 2 * apple_margin,
                                                square_size - 2 * apple_margin))
    return apple


def key_input(keyinput):
    global last_direction
    if keyinput == keyup and last_direction != (0, 1):
        print("UP")
        return (0, -1)
    elif keyinput == keydown and last_direction != (0, -1):
        print("DOWN")
        return (0, 1)
    elif keyinput == keyleft and last_direction != (1, 0):
        print("LEFT")
        return (-1, 0)
    elif keyinput == keyright and last_direction != (-1, 0):
        print("RIGHT")
        return (1, 0)
    else:
        return last_direction
        print("last direction")


def snake():
    global dead, ate_apple, score, apple_xy, last_direction
    last_head_x, last_head_y = snake_xy[-1]
    last_direction = direction
    print(last_direction)
    direction_x, direction_y = direction
    next_snake_xy = (last_head_x + direction_x, last_head_y + direction_y)
    if next_snake_xy[0] < 0 or next_snake_xy[0] > board_width - 1:
        dead = True
        print("0")
        return
    elif next_snake_xy[1] < 0 or next_snake_xy[1] > board_height - 1:
        dead = True
        print("1")
        return
    elif next_snake_xy in snake_xy and len(snake_xy) > 1:
        dead = True
        print("2")
        return
    elif next_snake_xy == apple_xy:
        ate_apple = True
        score += 1
        apple_xy = random_apple()
    snake_xy.append(next_snake_xy)
    render_snake()


def render_snake():
    global ate_apple
    head_x, head_y = snake_xy[-1]
    pygame.draw.rect(DISPLAYSURF, snake_head_color, (xmargin + head_x *
                                                     square_size + snake_margin, ymargin + head_y * square_size
                                                     + snake_margin, square_size - 2 * snake_margin,
                                                     square_size - 2 * snake_margin))
    if len(snake_xy) > 1:
        last_head_x, last_head_y = snake_xy[-2]
        pygame.draw.rect(DISPLAYSURF, snake_head_color, (xmargin + last_head_x
                                                         * square_size + snake_margin, ymargin + last_head_y *
                                                         square_size + snake_margin, square_size - 2 *
                                                         snake_margin, square_size - 2 * snake_margin))
    if not ate_apple and len(snake_xy) > 1:
        tail_x, tail_y = snake_xy.pop(0)
        if (tail_x + tail_y) % 2 == 0:
            draw_square(tail_x, tail_y, even_color)
        else:
            draw_square(tail_x, tail_y, odd_color)
    else:
        ate_apple = False


def update_score(n):
    pygame.display.set_caption("Snake  - score: " + str(n))


DISPLAYSURF = pygame.display.set_mode((board_width * square_size + xmargin * 2,
                                       board_height * square_size
                                       + ymargin * 2))

update_score(score)
background_grid()
pygame.draw.rect(DISPLAYSURF, apple_color, (xmargin + apple_xy[0] * square_size
                                            + apple_margin, ymargin +
                                            apple_xy[1] * square_size
                                            + apple_margin, square_size - 2 * apple_margin,
                                            square_size - 2 * apple_margin))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            direction = key_input(event.key)
    if not dead:
        snake()
        update_score(score)
    pygame.display.update()
    FPSCLOCK.tick(FPS)
