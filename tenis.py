#Python Tennis Game
#Author: Henry D

import turtle
import random
import time

x = 1

wn = turtle.Screen()
wn.bgcolor("lightgreen")

p1 = turtle.Turtle()
p2 = turtle.Turtle()
ball = turtle.Turtle()
p1.shape("square")
p2.shape("square")
ball.shape("circle")
ball.pu()
p1.pu()
p2.pu()

p1.bk(300)
p2.fd(300)
p1.lt(90)
p2.lt(90)
p1.color("blue")
p2.color("red")
ball.color("yellow")
ball.speed(0)

def hit():
    while x == 1:
        ball.fd(2)
        if ball.distance(p1) < 15:
            ball.lt(random.randint(160, 200))
        if ball.distance(p2) < 15:
            ball.lt(random.randint(160, 200))
        if ball.ycor() > 300:
            ball.lt(70)
        if ball.ycor() < -300:
            ball.lt(70)

def p1up():
    p1.fd(10)

def p1down():
    p1.bk(10)

def p2up():
    p2.fd(10)

def p2down():
    p2.bk(10)

wn.onkey(p1up, "w")
wn.onkey(p1down, "s")
wn.onkey(p2up, "Up")
wn.onkey(p2down, "Down")
wn.ontimer(hit, 1)

wn.listen()
wn.mainloop()
