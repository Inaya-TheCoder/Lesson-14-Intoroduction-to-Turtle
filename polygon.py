import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
a = 6
b = 19
angle = 360 / b
for i in range(b):
    polygon.forward(b)
    polygon.right(angle)
turtle.done()
