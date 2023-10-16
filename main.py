from turtle import Turtle, Screen
cursor=Turtle()
screen=Screen()
def move_forward():
    cursor.forward(10)
def move_back():
    cursor.back(10)
def turn_left():
    angle=cursor.heading()+10
    cursor.setheading(angle)
def turn_right():
    angle=cursor.heading()-10
    cursor.setheading(angle)
def clear():
    cursor.clear()
    cursor.penup()
    cursor.home()
    cursor.pendown()
screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_back, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=clear, key='c')




screen.exitonclick()
