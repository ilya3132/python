import pygame
from tkinter import *
import time
import random


pygame.init()

out = Tk()
out.title ("ping pong")
out.resizable()
canvas = Canvas(out,width = 1234,height = 1000,highlightthickness = 0)
out.wm_attributes('-topmost', 1)

canvas.pack()
out.update()

class Paddle:
    def  __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill = color)
        open = [40,80,90,100,150,170,200,250,300,350,400,450,500]
        self.starting_point_x = open [0]
        self.canvas.move(self.id,self.starting_point_x,250)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>',self.turn_RIGHT)
        self.canvas.bind_all('<KeyPress-Left>',self.turn_LEFT)
        self.canvas.bind_all('<KeyPress-RETURN>', self.turn_RETURN)


        self.started = False
    def turn_RIGHT(self,event):
        self.x = 3
    def turn_LEFT(self,event):
        self.x = -3
    def turn_RETURN(self,event):
        self.started = True
    def draw(self):
        self.canvas.move(self.id,self.x,0)




class sharik:
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.id,250,250)

        isaskhar = [1,2,-1,-2]
        random.shuffle(isaskhar)
        self.x = isaskhar [0]
        self.y = - 5
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False


    def floor (self,pos):
        paddle_pos = self.canvas.coords (self.paddle.id)
        if pos [2] >= paddle_pos [0] and  pos [0] <= paddle_pos [2]:
            if pos[3] >= paddle_pos[1] and  pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw (self):
        self.canvas.move (self.id,self.x,self.y)
        pos = self.canvas.cords (self.id)
        if pos[1] <= 0:
            self.y = 2
        if self.floor(pos) == True:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2

paddle = Paddle (canvas,'Green')
ball = sharik (canvas,paddle,'Green')
while not ball.hit_bottom:
    if paddle.started == True:
        ball.draw()
        paddle.draw()
    out.update_idletasks()
    out.update()
    time.sleep(0.01)
time.sleep(2)