#Challenges 
import turtle
#1. (Turtle: paint a smiley face) Write a program that paints a smiley face.
# Drawing outer circle
turtle.pensize(3)
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
# turtle.begin_fill() # Begin to fill color in a shape
turtle.color("black")
turtle.circle(100) # Draw a circle
turtle.end_fill()

#Drawing eyes
turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("black")
turtle.circle(15) # Draw a circle
turtle.end_fill()

turtle.penup()
turtle.goto(50, 100)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("black")
turtle.circle(15) # Draw a circle
turtle.end_fill()

# Drawing Nose
turtle.penup() # Pull the pen up
turtle.goto(0, 100)
turtle.left(180)
turtle.pendown() # Pull the pen down
#turtle.begin_fill() # Begin to fill color in a shape
turtle.color("black")
turtle.circle(40, steps = 3) # Draw a triangle
turtle.end_fill()


#Drawing smile 
turtle.penup() # Pull the pen up
turtle.goto(60, 50)
turtle.pendown()
turtle.left(45)
turtle.forward(85)
turtle.color("black")
turtle.width(3)

turtle.penup() # Pull the pen up
turtle.goto(-60, 50)
turtle.pendown()
turtle.left(90)
turtle.forward(85)
turtle.color("black")
turtle.width(3)


turtle.hideturtle()
turtle.done() 

#2. (Turtle: draw shapes) Write a program that draws a triangle, square, pentagon,
# hexagon, and octagon, as shown below. Note that the bottom edges of these shapes
# are parallel to the x-axis. (Hint: For a triangle with a bottom line parallel to the x-axis,
# set the turtle’s heading to 60 degrees.)

#3. (Financial application: payroll) Write a program that reads the following information
#and prints a payroll statement:
# Employee’s name (e.g., Smith)
# Number of hours worked in a week (e.g., 10)
# Hourly pay rate (e.g., 9.75)
# Federal tax withholding rate (e.g., 20%)
# State tax withholding rate (e.g., 9%)