# =========== TASK #3 ===================
# This function should decide if the game has ended.
# 'field' parameter is the same as in previous task, but you won't have 'CROSS' and 'CIRCLE' variables here to check against.
# But you don't really need them here anyway ;)
#
# For this function to work, it should return the correct value indicating the status of the game. Possible values are listed below:
# -1 - the game is not over yet
#  0 - a tie. The field is full but no one wins
#  1 - cross wins
#  2 - circle wins
def checkGameOver(field):
    return -1