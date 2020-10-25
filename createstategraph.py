import numpy as np
from config import ROWS, COLUMNS, symbolmap, States, moveStates, flatboard, playcount, statetree
from checkwins import didOwin, didXwin

def updateStates(inputboard):
    global States, moveStates, ROWS, symbolmap
    board = inputboard
    flag = 0

    if (((sum(board)) == 1) or ((sum(board)) == 0)) and (tuple(board) not in States.keys()):

        n = board.count(0)
        if n == 0:
            if didOwin(np.array(board).reshape((3, 3))) is False:
                moveStates[0].append(tuple(board[:]))
                playcount[0] += 1
                States[tuple(board[:])] = 0
        elif n == 1:
            if didXwin(np.array(board).reshape((3, 3))) is False:
                moveStates[1].append(tuple(board[:]))
                playcount[1] += 1
                States[tuple(board[:])] = 0
        elif n == 2:
            if didOwin(np.array(board).reshape((3, 3))) is False:
                moveStates[2].append(tuple(board[:]))
                playcount[2] += 1
                States[tuple(board[:])] = 0
        elif n == 3:
            if didXwin(np.array(board).reshape((3, 3))) is False:
                moveStates[3].append(tuple(board[:]))
                playcount[3] += 1
                States[tuple(board[:])] = 0
        elif n == 4:
            moveStates[4].append(tuple(board[:]))
            playcount[4] += 1
            States[tuple(board[:])] = 0
        elif n == 5:
            moveStates[5].append(tuple(board[:]))
            playcount[5] += 1
            States[tuple(board[:])] = 0
        elif n == 6:
            moveStates[6].append(tuple(board[:]))
            playcount[6] += 1
            States[tuple(board[:])] = 0
        elif n == 7:
            moveStates[7].append(tuple(board[:]))
            playcount[7] += 1
            States[tuple(board[:])] = 0
        elif n == 8:
            moveStates[8].append(tuple(board[:]))
            playcount[8] += 1
            States[tuple(board[:])] = 0


def enumerateStates(node):
    global flatboard
    for i in range(-1, 2, 1):
        flatboard[node] = i
        updateStates(flatboard)
        if node < 8:
            enumerateStates(node + 1)


def assigninitialrewards():
    global States
    for key in States.keys():
        if didXwin(np.asarray(key).reshape(3, 3)):
            States[key] = 1
        elif didOwin(np.asarray(key).reshape(3, 3)):
            States[key] = -1



def createstatetree():
    global statetree

    for key, value in moveStates.items():
        if key != 0:
            for statetuple1 in value:
                if didXwin(np.asarray(statetuple1).reshape(3,3)) or didOwin(np.asarray(statetuple1).reshape(3,3)):
                    pass
                else:
                    statetree[statetuple1] = []
                    for statetuple2 in moveStates[key-1]:
                        count = 0
                        for i in range(len(statetuple2)):
                            if statetuple1[i] == statetuple2[i]:
                                count = count+1
                        if count == (len(statetuple2) - 1):
                            statetree[statetuple1].append(list(statetuple2))





