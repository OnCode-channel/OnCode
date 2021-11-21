import turtle
from random import choice, randint

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=1.0,height=1.0)
window.bgcolor("black")
window.tracer(2)

border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()

border.goto(0,300)
border.color('white')
border.setheading(270)
for i in range(25):
    if i%2==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

rocket_a = turtle.Turtle()
rocket_a.color('white')
rocket_a.shape('square')
rocket_a.shapesize(stretch_len=1,stretch_wid=5)
rocket_a.penup()
rocket_a.goto(-450,0)

rocket_b = turtle.Turtle()
rocket_b.speed(100)
rocket_b.shape("square")
rocket_b.color("white")
rocket_b.shapesize(stretch_wid=5, stretch_len=1)
rocket_b.penup()
rocket_b.goto(450, 0)

FONT = ("Arial", 44)
score_a = 0
s1 = turtle.Turtle(visible=False)
s1.color('white')
s1.penup()
s1.setposition(-200, 300)
s1.write(score_a, font=FONT)

score_b = 0
s2 = turtle.Turtle(visible=False)
s2.color('white')
s2.penup()
s2.setposition(200, 300)
s2.write(score_a, font=FONT)

def move_up():
     y  = rocket_a.ycor() + 20
     if y > 250:
         y = 250
     rocket_a.sety(y)

def move_down():
    y = rocket_a.ycor() - 20
    if y < -250:
        y = -250
    rocket_a.sety(y)

def move_up_b():
    y = rocket_b.ycor() + 20
    if y > 250:
        y = 250
    rocket_b.sety(y)

def move_down_b():
    y = rocket_b.ycor() - 20
    if y < -250:
        y = -250
    rocket_b.sety(y)

ball = turtle.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('red')
ball.dx = 3
ball.dy = -3
ball.penup()

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_up_b, "Up")
window.onkeypress(move_down_b, "Down")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        score_b += 1
        s2.clear()
        s2.write(score_b, font=FONT)
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4,-3,-2, 2,3,4])
        ball.dy = choice([-4,-3,-2, 2,3,4])

    if ball.xcor() <= -490:
        score_a += 1
        s1.clear()
        s1.write(score_a, font=FONT)
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4,-3,-2, 2,3,4])
        ball.dy = choice([-4,-3,-2, 2,3,4])

    if ball.ycor() >= rocket_b.ycor()-50 and ball.ycor() <= rocket_b.ycor()+50 \
        and ball.xcor() >= rocket_b.xcor()-5 and ball.xcor() <= rocket_b.xcor()+5:
        ball.dx = -ball.dx

    if ball.ycor() >= rocket_a.ycor()-50 and ball.ycor() <= rocket_a.ycor()+50 \
        and ball.xcor() >= rocket_a.xcor()-5 and ball.xcor() <= rocket_a.xcor()+5:
        ball.dx = -ball.dx

window.mainloop()
