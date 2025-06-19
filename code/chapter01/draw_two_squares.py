import turtle

my_turtle = turtle.Turtle()

# First square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Move to a new location without drawing
my_turtle.penup()
my_turtle.goto(150, 150)
my_turtle.pendown()

# Second square with different color
my_turtle.color("blue")
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

turtle.done()
