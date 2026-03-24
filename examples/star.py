"""Simple star pattern with Python turtle."""
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star")

t = turtle.Turtle()
t.speed(0)
t.pencolor("yellow")
t.width(3)

for _ in range(5):
    t.forward(200)
    t.right(144)

turtle.done()
