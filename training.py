import random
from config import ROWS, COLUMNS, symbolmap, States, moveStates, flatboard, playcount, statetree
from matplotlib import pyplot as plot

def training():
    global States, statetree

    for episode in range(10):
        ALPHA = 0.8
        Stateslist = list(States.keys())
        random.shuffle(Stateslist)
        for key in Stateslist:
            if sum(key) == 0 and key in statetree.keys():
                for nextstate in statetree[key]:
                    if (States[tuple(nextstate)]*0.8) > States[key]:
                        States[key] = States[tuple(nextstate)]*ALPHA
            elif sum(key) == 1 and key in statetree.keys():
                for nextstate in statetree[key]:
                    if (States[tuple(nextstate)]*0.8) < States[key]:
                        States[key] = States[tuple(nextstate)]*ALPHA

    #     plot.hist(States.values(), bins=100)
    #     plot.pause(0.25)
#
# plot.show()