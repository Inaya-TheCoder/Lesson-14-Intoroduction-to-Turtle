import turtle
a = turtle.Screen()
a.bgcolor("pink")
a.title("Hello Everyone!")
b = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        b.fd(size + 1)
        b.left(90)
        size = size - 5
    size = size + 1
turtle.done()