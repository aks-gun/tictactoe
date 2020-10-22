import collections
import numpy as np

from displayboard import displayBoard

# from updateStates import updateStates

ROWS = 3
COLUMNS = 3

board = np.zeros((3, 3))
symbolmap = {1: "X", 0: "-", -1: "O"}

# displayBoard(board, ROWS, symbolmap)
States = []
flatboard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0


def updateStates():
    global flatboard, States
    flag = 0
    for elem in States:
        if collections.Counter(elem) == collections.Counter(flatboard):
            flag = 1
    if (flag == 1) or (abs(sum(flatboard)) > 1):
        pass
    else:
        States.append(flatboard)


def enumerateStates(node):
    global flatboard, States
    for i in range(-1, 2, 1):
        flatboard[node] = i
        updateStates()
        if node < 8:
            enumerateStates(node + 1)


enumerateStates(0)

print(States)
