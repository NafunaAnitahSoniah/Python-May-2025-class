"""
import turtle
turtle.forward(200) #pixels on the screen
turtle.left(90)       #angle
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)

#Turtle package is a function that programs a ccomputer to produce graphics

#ANOTHER EXAMPLE

t = turtle.Turtle()
t.speed(10)
screen = turtle.Screen()
screen.bgcolor("#800080")

def Draw_petal(turtle_obj, radius):
    turtle_obj.color("pink")
    turtle_obj.begin_fill()
    turtle_obj.circle(radius, 60)
    turtle_obj.left(180 - 60)
    turtle_obj.circle(radius, 60)
    turtle_obj.end_fill()

num_petal = 8
petal_radius = 70

for _ in range(num_petal):
    Draw_petal(t, petal_radius)
    t.left(360 / num_petal)

t.penup()
t.goto(0,0)
t.pendown()
t.color("yellow")
t.dot(30)
turtle.done()
"""

import turtle

# Create a turtle object and set up the screen
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=800, height=500)
t.speed(0) # Set drawing speed to fastest

# Define ring properties
ring_radius = 50
ring_thickness = 6
horizontal_offset = 110
vertical_offset = 50

# List of colors for the Olympic rings
colors = ["blue", "black", "red", "yellow", "green"]

# Function to draw a single ring
def draw_ring(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.pensize(ring_thickness)
    t.circle(ring_radius)

# Draw the top row of rings (blue, black, red)
draw_ring(-horizontal_offset, 0, colors[0]) # Blue
draw_ring(0, 0, colors[1]) # Black
draw_ring(horizontal_offset, 0, colors[2]) # Red


# Draw the bottom row of rings (yellow, green)
draw_ring(-horizontal_offset / 2, -vertical_offset, colors[3]) # Yellow
draw_ring(horizontal_offset / 2, -vertical_offset, colors[4]) # Green

# Hide the turtle and keep the window open until closed manually
t.hideturtle()
turtle.done()

