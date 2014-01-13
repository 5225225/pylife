import sys
import random
import time


def near(boarditem):
    x = int(boarditem[0])
    y = int(boarditem[1])
    found = 0
    #This is the slow bit, as far as I can tell.
    #This is the quickest way of doing it, though.
    if (x-1, y-1) in board:
        found += 1
    if (x-1, y) in board:
        found += 1
    if (x-1, y+1) in board:
        found += 1
    if (x, y-1) in board:
        found += 1
    if (x, y+1) in board:
        found += 1
    if (x+1, y-1) in board:
        found += 1
    if (x+1, y) in board:
        found += 1
    if (x+1, y+1) in board:
        found += 1
    return found


board = set()

chance = .25

xwidth = 100
ywidth = 100

stay = (2, 3)
born = (3, )

FPS = 100

for x in range(0, xwidth):
    for y in range(0, ywidth):
        if random.random() < chance:
            board.add((x, y))
tick = 0
starttime = time.time()
lastprint = 0

outstr = ""

while True:
    outstr = ""
    tick += 1
    newboard = board.copy()
    for x in range(0, xwidth):
        for y in range(0, ywidth):
            nearnum = near((x, y))
            if (x, y) in board:
                if nearnum not in stay:
                    newboard.discard((x, y))
            else:
                if nearnum in born:
                    newboard.add((x, y))

    board = newboard.copy()

    if time.time() - lastprint > 1/FPS:
        lastprint = time.time()
        for x in range(0, xwidth):
            for y in range(0, ywidth):
                if (x, y) in board:
                    outstr += "#"
                else:
                    outstr += "."
            outstr += "\n"
        sys.stdout.write(outstr)
        sys.stdout.flush()
        print("""
    POPULATION: {}
    TICK: {}
    TPS: {}""".format(
            len(board),
            tick,
            round(tick / (time.time() - starttime), 5)))
