import time
import curses
from acync_animation import blink, animate_spaceship
from acync_animation import fire
import random


TIC_TIMEOUT = 0.1

with open("./frames/rocket_frame_1.txt", "r") as file:
    frame1 = file.read()

with open("./frames/rocket_frame_2.txt", "r") as file:
    frame2 = file.read()

frames = [frame1, frame2]


def generate_stars_corounes(canvas, row, column, qty=100) -> list:
    stars = '+*.:'
    coroutines = []
    for _ in range(qty):
        rand_row = random.randint(1, row-1)
        rand_column = random.randint(1, column-1)
        rand_star = random.choice(stars)
        coroutines.append(blink(canvas, rand_row, rand_column, rand_star)) 
    return coroutines   


def draw(canvas):
    row, column = curses.window.getmaxyx(canvas)
    curses.curs_set(False)
    canvas.border()
    fire_coroutine = fire(canvas, row/2, column/2)
    space_ship_coroutine = animate_spaceship(canvas, row/2, column/2, frames)
    coroutines = generate_stars_corounes(canvas, row, column, qty=150)
    coroutines.append(space_ship_coroutine)
    coroutines.append(fire_coroutine)
    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__=='__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)

