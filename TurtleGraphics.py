from turtle import Turtle

t = Turtle()
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(300)
t.circle(50, 180)
t.right(45)
t.forward(150)
t.circle(50, 360)
t.forward(25)
t.circle(25, 360)
t.forward(100)
t.left(90)
t.forward(200)
t.circle(50, 270)
t.forward(100)
t.circle(150, 360)
t.left(90)
t.forward(150)
t.left(90)
t.forward(300)
t.left(135)
t.forward(200)
t.hideturtle()
t.write('My Python Turtle', move=True, align='center', font=('Freestyle Script', 50, 'normal'))


t.screen.exitonclick()