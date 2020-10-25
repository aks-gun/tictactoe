import numpy as np
from config import ROWS, COLUMNS, symbolmap, States, moveStates, flatboard, playcount, statetree

def didXwin(npboard):
    global ROWS
    if ROWS in npboard.sum(axis=0):
        return True
    elif ROWS in npboard.sum(axis=1):
        return True
    elif sum(npboard[i][i] for i in range(ROWS)) == ROWS or sum(npboard[i][ROWS - i - 1] for i in range(ROWS)) == ROWS:
        return True
    else:
        return False

def didOwin(npboard):
    global ROWS
    if -ROWS in npboard.sum(axis=0):
        return True
    elif -ROWS in npboard.sum(axis=1):
        return True
    elif sum(npboard[i][i] for i in range(ROWS)) == -ROWS or sum(npboard[i][ROWS - i - 1] for i in range(ROWS)) == -ROWS:
        return True
    else:
        return False