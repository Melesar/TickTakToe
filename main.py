import pygame
import math
import random
from check_win import checkGameOver

CROSS = 1
CIRCLE = 2

cellSize = 200
screenSize = 3 * cellSize
gridWidth = 4
elementWidth = 10

elementColor = (255, 255, 255)
gridColor = (243, 238, 7)
backgroundColor = (51, 204, 255)

aiDesicionTime = 500

def main():
    pygame.init()

    pygame.display.set_caption("Tick Tack Toe")

    running = True
    screen = pygame.display.set_mode((screenSize, screenSize))

    field = [[0 for x in range(3)] for y in range(3)]

    screen.fill(backgroundColor)
    pygame.draw.line(screen, gridColor, (cellSize, 0), (cellSize, screenSize), gridWidth)
    pygame.draw.line(screen, gridColor, (2 * cellSize, 0), (2 * cellSize, screenSize), gridWidth)
    pygame.draw.line(screen, gridColor, (0, cellSize), (screenSize, cellSize), gridWidth)
    pygame.draw.line(screen, gridColor, (0, 2 * cellSize), (screenSize, 2 * cellSize), gridWidth)

    playerInput = False
    isGameOver = False
    while running:
        drawField(field, screen)
        pygame.display.update()
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if isGameOver:
            continue

        if playerInput:
            pygame.time.wait(aiDesicionTime)
            aiStep(field)
            playerInput = False
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = event.pos
                # ======= TASK # 1 =========
                #
                # Here you need to insert a code that puts a cross in the cell that the player have just clicked.
                # The code that will do just that is below:
                #
                #   field[x][y] = CROSS
                #   playerInput = True
                #
                # where x,y are indexes of the cell in the field array. The tricky part is to calculate those :)
                # 
                # Hint: 'screenSize' variable holds the size of the entire screen and 'cellSize' variable holds the size of one cell in pixels.
                # The coordinate system starts in the top-left corner of the screen, X axis goes left, Y axis goes down. 'mousePosition' variable
                # is the (x, y) coordinates of the mouse click.
        
        gameStatus = checkGameOver(field)
        if gameStatus >= 0:
            isGameOver = True

        if gameStatus == 0:
            # Here goes tie
            continue
        elif gameStatus == CROSS:
            # Here goes win
            continue
        elif gameStatus == CIRCLE:
            # Here goes lose
            continue
    
def drawField(field, screen):
    for x in range(3):
        for y in range(3):
            coords = (x * cellSize, y * cellSize) 
            fieldValue = field[x][y]
            if fieldValue == CIRCLE:
                pygame.draw.circle(screen, elementColor, (coords[0] + 0.5 * cellSize, coords[1] + 0.5 * cellSize), cellSize * 0.5 * 0.8, elementWidth)
            if fieldValue == CROSS:
                drawCross(screen, coords)

def drawCross(screen, coords):
    offset = math.sqrt(2) * cellSize * 0.5 * 0.1
    start1 = (coords[0] + offset, coords[1] + offset)
    end1 = (coords[0] + cellSize - offset, coords[1] + cellSize - offset)
    start2 = (coords[0] + offset, coords[1] + cellSize - offset)
    end2 = (coords[0] + cellSize - offset, coords[1] + offset)
    pygame.draw.line(screen, elementColor, start1, end1, elementWidth)
    pygame.draw.line(screen, elementColor, start2, end2, elementWidth)

def aiStep(field):
    # ========= TASK #2 ===========
    # Here you should make a turn for the AI opponent.
    # For now let's make a pretty dumb AI that will just pick a random empty cell and put a circle in there.
    # Again, the code that does it is the following:
    #   
    #   field[x][y] = CIRCLE
    #
    # The task to calculate x,y is again on you :) 
    #
    # 'field' parameter is a two-dimensional array of integers of size 3x3 where
    # 0 - empty field
    # 1 - cross. Use 'CROSS' variable to check for this
    # 2 - circle. Use 'CIRCLE' variable to check for this
    #
    # If this dumb AI is too easy for you and you want to challenge yourself a bit more, you may implement
    # a more reasonable one, but only after you finish this task and the next one :)
    pass

if __name__ == "__main__":
    main()