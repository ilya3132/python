import pygame

pygame.init

win = pygame.display.set_mode((1280,1024))
walkLeft = [pygame.image.load('golden knight walk animation with sword face left_00001.png'),pygame.image.load('golden knight walk animation with sword face left_00002.png'),
            pygame.image.load('golden knight walk animation with sword face left_00003.png'),pygame.image.load('golden knight walk animation with sword face left_00004.png'),
            pygame.image.load('golden knight walk animation with sword face left_00005.png'),pygame.image.load('golden knight walk animation with sword face left_00006.png'),
            pygame.image.load('golden knight walk animation with sword face left_00007.png'),pygame.image.load('golden knight walk animation with sword face left_00008.png'),
            pygame.image.load('golden knight walk animation with sword face left_00009.png'),pygame.image.load('golden knight walk animation with sword face left_00010.png.'),
            pygame.image.load('golden knight walk animation with sword face left_00011.png'),pygame.image.load('golden knight walk animation with sword face left_00012.png'),
            pygame.image.load('golden knight walk animation with sword face left_00013.png')]




walkRight = [pygame.image.load('golden knight animation sword right edit_00001.png'),pygame.image.load('golden knight animation sword right edit_00002.png'),
            pygame.image.load('golden knight animation sword right edit_00003.png'),pygame.image.load('golden knight animation sword right edit_00004.png'),
            pygame.image.load('golden knight animation sword right edit_00005.png'),pygame.image.load('golden knight animation sword right edit_00006.png'),
            pygame.image.load('golden knight animation sword right edit_00007.png'),pygame.image.load('golden knight animation sword right edit_00008.png'),
            pygame.image.load('golden knight animation sword right edit_00009.png'),pygame.image.load('golden knight animation sword right edit_00010.png'),
            pygame.image.load('golden knight animation sword right edit_00011.png'),pygame.image.load('golden knight animation sword right edit_00012.png'),
            pygame.image.load('golden knight animation sword right edit_00013.png')]
bg = pygame.image.load('bg5.jpg')

speed = 20
weight = 50
x = 250
y = 250
height = 30

noOrYesJump = False
jump = 10

right = False
left  = False

frame = 0

def drawWindow():
    global frame
    win.blit(bg,(0,0))

    if frame +1 >= 13:
        frame = 0
    if left:
        win.blit(walkLeft [frame//1],(x,y))
        frame+= 1
    else:
        win.blit(walkRight[frame//1],(x,y))
        frame+= 1
    pygame.display.update()

play = True
while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play =False
    pygame.time.delay(100)

    keycups = pygame.key.get_pressed()

    if not (noOrYesJump):
        if keycups[pygame.K_w] and y > 5:
            y -= speed
        if keycups[pygame.K_s] and y < 500 - height - 5:
            y += speed
        if keycups[pygame.K_SPACE]:
            noOrYesJump = True
    else:
        if jump >=-10:
            if jump <0:
                y += ( jump ** 2) //2
            else:
                y -= ( jump ** 2) //2
            jump -= 1
        else:
            noOrYesJump = False
            jump = 10
    if keycups[pygame.K_a] and x > 5:
        x -= speed
        left= True
        right= False
    if keycups[pygame.K_d] and x < 500 - weight -5:
        x += speed
        left= False
        right= True

    drawWindow()

pygame.quit()


