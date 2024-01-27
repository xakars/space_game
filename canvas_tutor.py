import time
import curses
from acync_animation import blink


TIC_TIMEOUT = 0.1

def draw(canvas):
    row, column = (5, 20)
    curses.curs_set(False)
    canvas.border()
    coroutines = [blink(canvas, row, column+i, '*') for i in range(5)]
    while True:
        for coroutine in coroutines.copy():
            coroutine.send(None)
            canvas.refresh()
        time.sleep(TIC_TIMEOUT)

if __name__=='__main__':
    curses.update_lines_cols()
    print(curses.window.getmaxyx())
    curses.wrapper(draw)



