import sys
import random
import time

def near(boarditem):
    sitem = boarditem.partition(":")
    x = int(sitem[0])
    y = int(sitem[2])
    found = 0
    #This is the slow bit, as far as I can tell.
    #This is the quickest way of doing it, though.
    if "{}:{}".format(x-1,y-1) in board: found += 1 
    if "{}:{}".format(x-1,y) in board: found += 1
    if "{}:{}".format(x-1,y+1) in board: found += 1
    if "{}:{}".format(x,y-1) in board: found += 1
    if "{}:{}".format(x,y+1) in board: found += 1
    if "{}:{}".format(x+1,y-1) in board: found += 1
    if "{}:{}".format(x+1,y) in board: found += 1
    if "{}:{}".format(x+1,y+1) in board: found += 1

    return found



board = set()

chance = .25

xwidth = 40
ywidth = 170

stay = (2,3)
born = (3,)

FPS = 99

for x in range(0,xwidth):
    for y in range(0,ywidth):
        if random.random() < chance:
            board.add("{}:{}".format(x,y))
tick = 0
starttime = time.time()
lastprint = 0

outstr = ""

while True:
    outstr = ""
    tick += 1
    newboard = board.copy()
    for x in range(0,xwidth):
        for y in range(0,ywidth):
            xystr = "{}:{}".format(x,y)
            
            nearnum = near(xystr)
            if xystr in board:
                if nearnum not in stay:
                    newboard.discard(xystr)
            else:
                if nearnum in born:
                    newboard.add(xystr)

    board = newboard.copy()
    
    if time.time() - lastprint > 1/FPS :
        lastprint = time.time()
        for x in range(0,xwidth):
            for y in range(0,ywidth):
                if "{}:{}".format(x,y) in board:
                    outstr += "#"
                else:
                    outstr += "."
            outstr += "\n"
        print("\n"*99)
        sys.stdout.write(outstr)
        sys.stdout.flush()
        print("""
    POPULATION: {}
    TICK: {}
    TPS: {}""".format(len(board), tick, round(tick / (time.time() - starttime), 2)) )

