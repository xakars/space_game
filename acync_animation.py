import asyncio
import curses


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(10):
            await asyncio.sleep(0)
        canvas.addstr(row, column, symbol)
        for _ in range(10):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(10):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(10):
            await asyncio.sleep(0)
