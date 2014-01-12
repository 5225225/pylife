import sys
import random
import time

def near(boarditem):
    sitem = boarditem.split(":")
    x = int(sitem[0])
    y = int(sitem[1])
    found = 0

    
    return found



board = set()

chance = .25

xwidth = 40
ywidth = 170

stay = (2,3)
born = (3,)

for x in range(0,xwidth):
    for y in range(0,ywidth):
        if random.random() < chance:
            board.add("{}:{}".format(x,y))
tick = 0
starttime = time.time()

outstr = ""
for x in range(0,xwidth):
    for y in range(0,ywidth):
        if "{}:{}".format(x,y) in board:
            outstr += "#"
        else:
            outstr += "."
    outstr += "\n"

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
TICK:       {}
TPS:        {}""".format(len(board), tick, round(tick / (time.time() - starttime), 2)) )
