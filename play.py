import numpy as np
from results import displayBoard
from config import ROWS, COLUMNS, symbolmap, States, moveStates, flatboard, playcount, statetree
from checkwins import didXwin, didOwin

def makeaplay():
    global statetree, States, flatboard
    print("Hmm.. Now my turn")
    maxvalue = -2.0
    maxstate = []
    for n in statetree[tuple(flatboard)]:
        if States[tuple(n)] >= maxvalue:
            maxvalue = States[tuple(n)]
            maxstate = n
    flatboard = maxstate
    displayBoard(np.array(flatboard).reshape((3, 3)))

def getaninput():
    global flatboard, ROWS
    print("Now your turn")
    a = input("Enter row:")
    b = input("Enter column:")
    flatboard[(int(a) - 1) * ROWS + int(b) - 1] = -1
    displayBoard(np.array(flatboard).reshape((3, 3)))

def playwithuser():
    global flatboard
    noonewon = True
    boardnotfull = True
    flatboard[:] = [0]*len(flatboard)
    print("Hey, let's play tictactoe")
    print("My turn")
    flatboard[0] = 1
    displayBoard(np.array(flatboard).reshape((3, 3)))
    while True:
        getaninput()
        if didOwin(np.array(flatboard).reshape(3,3)):
            print("YOU WON!!")
            break
        makeaplay()
        if didXwin(np.array(flatboard).reshape(3,3)):
            print("I WON!!")
            break
        if flatboard.count(0) == 0:
            print("Hmm.. looks like it's a draw!!")
            break




