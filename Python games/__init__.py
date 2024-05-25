import pygame

pygame.init

win = pygame.display.set_mode((700,500))
speed = 20
weight = 50
x = 250
y = 250
height = 30

noOrYesJump = False
jump = 10

right = False
left  = False

def drawWindow():
    win.blit((0,0))

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
    if keycups[pygame.K_d] and x < 500 - weight -5:
        x += speed
    pygame.draw.rect(win,(87, 27, 167), (x,y,weight,height))
    pygame.display.update()
    win.fill((0, 0, 255))
pygame.quit()


