"""Colorful spiral drawn with Python turtle."""
import turtle
import sys; sys.path.insert(0, ".")
import save_png

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral")

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

for i in range(360):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 0.5)
    t.left(59)

save_png.save(screen, "spiral")
turtle.exitonclick()
