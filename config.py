ROWS = 3
COLUMNS = 3

symbolmap = {1: "X", 0: "-", -1: "O"}

States = {}
moveStates = {i: [] for i in range(ROWS * COLUMNS)}
flatboard = [0] * ROWS * COLUMNS
playcount = [0] * ROWS * COLUMNS
statetree = {}

