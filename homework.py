import turtle
turtle.Screen()
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(400,450)
poly = turtle.Turtle()
a = 20
b = 20
angle = 360 / 4
for i in range(b):
    poly.forward(b)
    poly.right(angle)
turtle.done()

