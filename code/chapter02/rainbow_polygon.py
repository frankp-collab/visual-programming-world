"""
Chapter 2: Python Basics Through Art
Example: Rainbow Polygon with Variables

This program demonstrates how variables make code flexible.
You can easily change the shape, size, and colors!
"""

import turtle

# Create our artist turtle
artist = turtle.Turtle()
artist.speed(6)
artist.pensize(3)

# Variables make our code flexible!
sides = 6                # Try changing this to 3, 4, 5, 8, etc.
size = 80               # Try 50, 100, 120, etc.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Calculate the turn angle (this works for any number of sides!)
angle = 360 / sides

print(f"Drawing a {sides}-sided polygon!")
print(f"Each side will be {size} pixels long")
print(f"I'll turn {angle} degrees at each corner")

# Draw the polygon with different colored sides
for i in range(sides):
    # Choose a color from our list
    color_index = i % len(colors)  # This cycles through colors
    artist.color(colors[color_index])
    
    # Draw one side
    artist.forward(size)
    artist.right(angle)
    
    print(f"Drew side {i+1} in {colors[color_index]} color")

print("🎨 Rainbow polygon complete!")
print("💡 Try changing the variables at the top and run again!")

# Keep the window open
turtle.done()
