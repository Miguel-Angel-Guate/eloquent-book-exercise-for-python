board = ""
for x in range (0,9):
    for y in range (0,8):
        if (x+y) % 2 == 0:
            board += " "
        else:
            board += "#"
    board += "\n"
    print(board)