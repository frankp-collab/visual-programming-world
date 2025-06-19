"""
Chapter 3: Loops - The Magic of Automation
Example: Growing Spiral with Color Changes

This shows the power of loops to create complex patterns
with just a few lines of code!
"""

import turtle

# Set up our canvas
screen = turtle.Screen()
screen.bgcolor("black")  # Black background makes colors pop!
screen.setup(width=800, height=600)

# Create our spiral artist
spiral_artist = turtle.Turtle()
spiral_artist.speed(0)  # Fastest speed
spiral_artist.pensize(2)

# Color list for our rainbow spiral
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta", "white"]

# Starting values
distance = 5
angle = 91  # Slightly more than 90 degrees creates the spiral effect

print("🌀 Creating a growing rainbow spiral!")
print("Watch as loops create complex art from simple rules...")

# The magic loop!
for i in range(100):
    # Choose color (cycles through our color list)
    color_index = i % len(colors)
    spiral_artist.color(colors[color_index])
    
    # Draw part of the spiral
    spiral_artist.forward(distance)
    spiral_artist.right(angle)
    
    # Make each step slightly longer (this creates the "growing" effect)
    distance = distance + 2
    
    # Print progress every 10 steps
    if (i + 1) % 10 == 0:
        print(f"Completed {i + 1} steps of the spiral...")

print("✨ Spiral complete!")
print("🔄 This pattern was created with just one loop!")
print("💡 Try changing the angle or distance growth for different effects!")

# Keep the window open
screen.exitonclick()
