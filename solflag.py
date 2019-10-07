import turtle
clr=turtle.Turtle()

clr.color("white","orange")

wn=turtle.Screen()
wn.bgcolor('black')
wn.title("Jai Hind")
wn.bgpic('army.png')
clr.up()
clr.goto(-100,0)
clr.goto(-120,-30)
clr.down()
clr.goto(-120,-30)
clr.goto(-120,280)
clr.setheading(90)
clr.speed(1)

def rec(color):
    clr.begin_fill()
    clr.fillcolor(color)

    for i in range(2):
        clr.right(90)
        clr.forward(150)
        clr.right(90)
        clr.forward(40)
    clr.end_fill()
        

rec('orange')
clr.backward(40)
rec('white')
clr.backward(40)
rec('green')
clr.right(90)


clr.begin_fill()
clr.fillcolor('blue')

clr.forward(75)
clr.circle(20)
clr.end_fill()
clr.hideturtle()


turtle.done()