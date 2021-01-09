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

    font = pygame.font.SysFont(None, 72)

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
                x = int(event.pos[0] / cellSize)
                y = int(event.pos[1] / cellSize)
                if field[x][y] == 0:
                    field[x][y] = CROSS
                playerInput = True
        
        gameStatus = checkGameOver(field)
        if gameStatus >= 0:
            isGameOver = True

        if gameStatus == 0:
            # Here goes tie
            renderText("Tie", font, screen)
        elif gameStatus == CROSS:
            # Here goes win
            renderText("You won", font, screen)
        elif gameStatus == CIRCLE:
            # Here goes lose
            renderText("You lost", font, screen)
    
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

def renderText(text, font, screen):
    textImg = font.render(text, True, (255, 0, 0))
    rect = textImg.get_rect()
    coords = ((screenSize  - rect.size[0]) * 0.5, (screenSize - rect.size[1]) * 0.5)
    screen.blit(textImg, coords + rect.size)

def aiStep(field):
    emptyCells = []
    for x in range(3):
        for y in range(3):
            if field[x][y] == 0:
                emptyCells.append((x, y))
    
    if emptyCells:
        cell = random.choice(emptyCells)
        field[cell[0]][cell[1]] = CIRCLE

if __name__ == "__main__":
    main()