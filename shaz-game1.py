# Turtle Graphics Game – Space
import turtle

# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('navy')
# Create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup()
# Set speed variable
speed = 1
# Set speed variable
speed = 1
while True:
   player.forward(speed)