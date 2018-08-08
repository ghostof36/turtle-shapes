import turtle


alex = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightgreen")
response = input("What sided shape would you like Alex the Turtle to make? ")
turns = int(response)

if turns < 3:
    turns = 3
    print("Sorry, math says you need at least three sides.")

distance = 600 / turns
degrees = 360 / turns

#this moves the turtle a variable distance based on the number of sides
#in order to keep the entire shape perimeter equal to 600 pixels
for x in range(turns):
    alex.forward(distance)
    alex.left(degrees)

screen.exitonclick()