"""Simple star pattern with Python turtle."""
import turtle
import sys; sys.path.insert(0, ".")
import save_png

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

save_png.save(screen, "star")
turtle.exitonclick()
