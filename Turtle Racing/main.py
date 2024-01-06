from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput("Turtle Betting", "Bet on which color turtle is going to win")


turtleColors = ["red", "yellow", "orange", "green", "blue", "purple", "pink"]

y_val = -160
turtleNames = []

def setupFinishLine():
    matcher = Turtle()
    matcher.color("black")
    matcher.width(5)
    matcher.penup()
    matcher.goto(x=220, y=200)
    matcher.pendown()
    matcher.goto(x=220, y=-200)

setupFinishLine()


for i in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtleColors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_val)
    y_val += 50
    turtleNames.append(new_turtle)

race_on = False
if user_bet:
    race_on = True

while race_on:
    for turtle in turtleNames:
        forward_distance = random.randint(0, 15)
        turtle.forward(forward_distance)
        if turtle.xcor() > 230:
            print(turtle.color())
            race_on = False
            break









# for turtle in turtleNames:
#     turtle.penup()
#     turtle.goto(-230, y_val)
#     y_val += 50
#     turtle.pendown()







screen.exitonclick()