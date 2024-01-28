import time
import curses
from acync_animation import blink
import random


TIC_TIMEOUT = 0.1


def generate_stars_corounes(canvas, row, column, qty=100) -> list:
    stars = '+*.:'
    coroutines = []
    for _ in range(100):
        rand_row = random.randint(0, row-5)
        rand_column = random.randint(0, column-5)
        rand_star = random.choice(stars)
        coroutines.append(blink(canvas, rand_row, rand_column, rand_star)) 
    return coroutines   


def draw(canvas):
    row, column = curses.window.getmaxyx(canvas)
    curses.curs_set(False)
    canvas.border()
    coroutines = generate_stars_corounes(canvas, row, column, qty=50)
    while True:
        for coroutine in coroutines.copy():
            coroutine.send(None)
            canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__=='__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)

