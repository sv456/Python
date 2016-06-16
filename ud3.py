import turtle
def flower():
    window=turtle.Screen()
    window.bgcolor("red")
    baid=turtle.Turtle()
    baid.shape("turtle")
    baid.speed(15)
    baid.color("green")
    for i in range(50):
        baid.forward(200)
        baid.left(170)
    magie=turtle.Turtle()
    magie.shape("arrow")
    magie.penup()
    magie.forward(100)
    magie.pendown()
    magie.pensize(4)
    magie.right(90)
    magie.forward(200)
    window.exitonclick()

flower()
    
