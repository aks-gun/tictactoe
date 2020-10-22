def displayBoard(board, ROWS, symbolmap):
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
