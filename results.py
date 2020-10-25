import numpy as np
import matplotlib.pyplot as plot
from config import ROWS, COLUMNS, symbolmap, States, moveStates, flatboard, playcount, statetree

def displaymovestats():
    global playcount, moveStates, States

    for key, value in States.items():
        print(key, ":", value)

    print("Total number of valid states with X playing first = ", len(States))

    print("Total number of possible first moves = ", len(moveStates[8]))
    print("Total number of possible second move = ", len(moveStates[7]))
    print("Total number of possible third move = ", len(moveStates[6]))
    print("Total number of possible fourth move = ", len(moveStates[5]))
    print("Total number of possible fifth move = ", len(moveStates[4]))
    print("Total number of possible sixth move = ", len(moveStates[3]))
    print("Total number of possible seventh move = ", len(moveStates[2]))
    print("Total number of possible eighth move = ", len(moveStates[1]))
    print("Total number of final states with a complete board = ", len(moveStates[0]))

    plot.bar(range(len(playcount), 0, -1), playcount)
    plot.xlabel("Stage of game")
    plot.ylabel("Number of possible moves")
    plot.title("Energy output from various fuel sources")
    plot.show()

def displayBoard(board):
    global ROWS, symbolmap
    for i in range(ROWS):
        print(" ", 2 * " ", end="")
        print(symbolmap[board[i, 0]], 2 * " ", end="")
        print("|", 2 * " ", end="")
        print(symbolmap[board[i, 1]], 2 * " ", end="")
        print("|", 2 * " ", end="")
        print(symbolmap[board[i, 2]], 2 * " ", end="")
        print(" ")
        if i != ROWS - 1:
            print(25 * "-")

def displaypossiblewinstates():

    global States
    for key, value in States.items():
        if value == 1:
            print(np.asarray(key).reshape(3, 3))
