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
# hexagon, and octagon. Note that the bottom edges of these shapes
# are parallel to the x-axis. (Hint: For a triangle with a bottom line parallel to the x-axis,
# set the turtle’s heading to 60 degrees.)
import turtle

# Drawing triangle
turtle.pensize(3)
turtle.penup() # Pull the pen up
turtle.goto(-150, -25)
turtle.left(180)
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("red")
turtle.circle(30, steps = 3) # Draw a triangle
turtle.end_fill()


# Drawing square
turtle.penup()
turtle.goto(-85, -25)
turtle.left(45)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("blue")
turtle.circle(30, steps=4) # Draw a circle
turtle.end_fill()

# Drawing pentagon
turtle.penup()
turtle.goto(0, -25)
#turtle.left(45)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("yellow")
turtle.circle(30, steps=5) # Draw a circle
turtle.end_fill()

# Drawing hexagon
turtle.penup()
turtle.goto(85, -25)
#turtle.left(-90)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("green")
turtle.circle(30, steps=6) # Draw a circle
turtle.end_fill()

# Drawing octagon
turtle.penup()
turtle.goto(170, -25)
#turtle.left(-90)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("purple")
turtle.circle(30, steps=8) # Draw a circle
turtle.end_fill()


turtle.hideturtle()
turtle.done() 



#3. (Financial application: payroll) Write a program that reads the following information
#and prints a payroll statement:
# Employee’s name (e.g., Smith)
# Number of hours worked in a week (e.g., 10)
# Hourly pay rate (e.g., 9.75)
# Federal tax withholding rate (e.g., 20%)
# State tax withholding rate (e.g., 9%)
import turtle

# Employee Name Heading
turtle.color("green")
turtle.penup()
turtle.goto(-300, 250)
turtle.pendown()
turtle.write("Employee Name", 
  font = ("Times", 18, "bold"))

# Employee Name Value
turtle.color("green")
turtle.penup()
turtle.goto(100, 250)
turtle.pendown()
turtle.write("Smith", 
  font = ("Times", 18, "bold"))

# Number of hours worked in a week. Heading.
turtle.color("green")
turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
turtle.write("Number of hours worked in a week:", 
  font = ("Times", 18, "bold"))

# Number of hours worked in a week Value
turtle.color("green")
turtle.penup()
turtle.goto(100, 200)
turtle.pendown()
turtle.write("10", 
  font = ("Times", 18, "bold"))

# Hourly pay rate. Heading.
turtle.color("green")
turtle.penup()
turtle.goto(-300, 150)
turtle.pendown()
turtle.write("Hourly pay rate:", 
  font = ("Times", 18, "bold"))

# Hourly pay rate Value
turtle.color("green")
turtle.penup()
turtle.goto(100, 150)
turtle.pendown()
turtle.write("9.75", 
  font = ("Times", 18, "bold"))

# Federal tax withholding rate. Heading.
turtle.color("green")
turtle.penup()
turtle.goto(-300, 100)
turtle.pendown()
turtle.write("Federal tax withholding rate:", 
  font = ("Times", 18, "bold"))

# Federal tax withholding rate. Value
turtle.color("green")
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.write("20%", 
  font = ("Times", 18, "bold"))

# State tax withholding rate. Heading.
turtle.color("green")
turtle.penup()
turtle.goto(-300, 50)
turtle.pendown()
turtle.write("State tax withholding rate:", 
  font = ("Times", 18, "bold"))

# State tax withholding rate. Value
turtle.color("green")
turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.write("9%", 
  font = ("Times", 18, "bold"))

turtle.hideturtle()
turtle.done() 