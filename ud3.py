import turtle
def draw_square(some):
    i=1
    while i<=4:
        some.forward(100)
        some.right(90)
        i+=1

def art():
    brad=turtle.Turtle()
    window=turtle.Screen()
    window.bgcolor("yellow")
    brad.color("blue")
    brad.shape("turtle")
    brad.speed(4)
    while (1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

art()
