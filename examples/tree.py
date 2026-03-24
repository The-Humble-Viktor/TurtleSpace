"""Recursive fractal tree drawn with Python turtle."""
import turtle


def draw_tree(t, branch_len, angle, shrink):
    if branch_len < 5:
        return
    t.forward(branch_len)
    t.left(angle)
    draw_tree(t, branch_len * shrink, angle, shrink)
    t.right(angle * 2)
    draw_tree(t, branch_len * shrink, angle, shrink)
    t.left(angle)
    t.backward(branch_len)


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree")

t = turtle.Turtle()
t.speed(0)
t.pencolor("green")
t.width(2)
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()

draw_tree(t, 100, 25, 0.75)

turtle.exitonclick()
