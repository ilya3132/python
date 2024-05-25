import pygame,random,sys
from pygame.locals import *

fps = 15
hight = 640
weight = 480
cellsize = 20
assert hight % cellsize == 0
assert weight % cellsize == 0
cellhight  = int (hight/cellsize)
cellweight = int (weight/cellsize)


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


white =(255,255,255)
black =(0,0,0)
green =(0, 255, 104)
red =(254, 0, 0)
background = black

head = 0 #Координаты головы

def main():
    global fpsclock,displaysurf,basicfont

    pygame.init()
    fpsclock = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((hight,weight))

    while True:
        rungame()

def terminate():
    pygame.quit()
    sys.exit()

def randomapple():
    return{'x': random.randint(0,cellweight-1),'y': random.randint(0,cellhight-1)}

def rungame():
    startx = random.randint(5,cellweight-6)
    starty = random.randint(5,cellhight-6)
    apple = randomapple()


    snakecoords = [{'x': startx, 'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if(event.key == K_LEFT or event.key == K_a)and direction != RIGHT:
                    direction = LEFT
                elif(event.key == K_RIGHT or event.key == K_d)and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
        if snakecoords [head]['x'] == -1 or snakecoords [head]['x'] == cellweight or snakecoords [head]['y'] == -1 or snakecoords [head]['y'] == cellhight:
            return
        for snakeBody in snakecoords [1:]:
            if snakeBody['x'] == snakecoords [head]['x'] and snakeBody['y'] == snakecoords[head]['y']:
                return
        if snakecoords[head]['x'] == apple['x'] and snakecoords[head]['x'] == apple['y']:
            apple = randomapple()
        else:
            del snakecoords[-1]

        if direction == UP:
            newHead = {'x': snakecoords[head]['x'], 'y': snakecoords[head]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': snakecoords[head]['x'], 'y': snakecoords[head]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': snakecoords[head]['x'] - 1, 'y': snakecoords[head]['y']}
        elif direction == RIGHT:
            newHead = {'x': snakecoords[head]['x'] + 1, 'y': snakecoords[head]['y']}

        snakecoords.insert (0,newHead)
        drawline()
        drawsnake(snakecoords)
        displaysurf.fill(background)
        pygame.display.update()
        fpsclock.tick(fps)



def drawsnake(snakecoords):
    for coords in snakecoords:
        x = coords ['x']*cellsize
        y = coords['y'] * cellsize
        wormSegmentRect = pygame.Rect(x, y,cellsize, cellsize)
        pygame.draw.rect(displaysurf, white, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, cellsize - 8, cellsize - 8)
        pygame.draw.rect(displaysurf, green, wormInnerSegmentRect)


def drawline():
    for x in range(0,weight,cellsize):
        pygame.draw.line(displaysurf,red,(x,0),(x,weight))


    for y in range(0, hight, cellsize):
        pygame.draw.line(displaysurf, red, (y, 0), (y, hight))




































if __name__ == '__main__':
    main()
