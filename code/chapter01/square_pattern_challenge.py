import turtle

my_turtle = turtle.Turtle()

colors = ["red", "green", "blue", "purple"]
start_x = -150
for i in range(4):
    my_turtle.penup()
    my_turtle.goto(start_x + i * 100, 0)
    my_turtle.pendown()
    my_turtle.color(colors[i % len(colors)])
    for _ in range(4):
        my_turtle.forward(50)
        my_turtle.right(90)

turtle.done()
