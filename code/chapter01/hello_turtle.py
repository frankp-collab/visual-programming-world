"""
Chapter 1: Your First Turtle Program
Run this to see your first piece of computer art!
"""

import turtle

# Create a turtle
my_turtle = turtle.Turtle()

# Draw a square
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Keep window open
turtle.done()

print("🎉 You just created your first computer art!")
