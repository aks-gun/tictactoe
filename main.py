import numpy as np
import random
from matplotlib import pyplot as plot
from config import ROWS, COLUMNS, symbolmap, States, moveStates, flatboard, playcount, statetree
from results import displayBoard, displaymovestats, displaypossiblewinstates
from createstategraph import enumerateStates, assigninitialrewards, createstatetree
from training import training
from play import playwithuser

# Sample displayboard example

enumerateStates(0)
# displaymovestats()
assigninitialrewards()
# displaypossiblewinstates()
createstatetree()
training()
# for value in statetree[(1,1,-1,0,-1,0,0,0,0)]:
#     print(States[tuple(value)])
#     displayBoard(np.asarray(value).reshape((3, 3)))
# for key, value in States.items():
#     if key.count(0) == 4:
#         print(value)
# print(States[(1,1,-1,1,-1,0,0,0,0)])
# displayBoard(np.array([1,1,-1,1,-1,0,0,0,0]).reshape((3, 3)))
# print(States[(1,1,-1,0,-1,0,1,0,0)])
# displayBoard(np.array([1,1,-1,0,-1,0,1,0,0]).reshape((3, 3)))
playwithuser()







