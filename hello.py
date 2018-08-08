import turtle

#define variables
alex = turtle.Turtle()
turns = input("What sided shape would you like Alex the Turtle to make? ")
t = int(turns)
f = 600 / t
d = 360 / t

#define background color
turtle.bgcolor("lightgreen")


for x in range(t):
    alex.forward(f)
    alex.left(d)

turtle.exitonclick()