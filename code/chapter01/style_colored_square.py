import turtle

my_turtle = turtle.Turtle()
my_turtle.color("red")       # Try "blue", "green", "purple"
my_turtle.pensize(5)         # Try different thickness

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

turtle.done()
