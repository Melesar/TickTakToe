# This should decide if the game has ended
#
# field is a two-dimensional array 3x3 where
# 0 - empty field
# 1 - cross
# 2 - circle
#
# The return value should be one of the following:
# -1 - the game is not over yet
#  0 - a tie. The field is full but no one wins
#  1 - cross wins
#  2 - circle wins
def checkGameOver(field):
    #check all columns
    for x in range(3):
        if field[x][0] * field[x][1] * field[x][2] != 0 and\
            field[x][0] == field[x][1] == field[x][2]:
            return field[x][0]
    
    #check all rows
    for y in range(3):
        if field[0][y] * field[1][y] * field[2][y] != 0 and\
            field[0][y] == field[1][y] == field[2][y]:
            return field[0][y]
    
    #check diagonals
    if field[0][0] * field[1][1] * field[2][2] != 0 and\
        field[0][0] == field[1][1] == field[2][2] or\
        field[2][0] * field[1][1] * field[0][2] != 0 and\
        field[2][0] == field[1][1] == field[0][2]:
        return field[1][1]
    
    #no win, so check if there is a space left
    for x in range(3):
        for y in range(3):
            if field[x][y] == 0:
                return -1

    return 0