
import turtle
a = int(input())
n = 0
c = float(input())
player = turtle.Turtle("turtle")
while n < a:
    player.forward(120)
    player.left(180)
    player.forward(120)
    player.left(180)
    player.left(c)
player.screen.mainloop()