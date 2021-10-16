import turtle

a=turtle.Turtle()
a.getscreen().bgcolor("black")

a.penup()
a.goto( -200, 100)
a.pendown()
a.color("grey")
a.speed(25)

def star (turtle, size):
    if size <=10:
        return

    else:
        turtle.fillcolor()
        for i in range (5):
            turtle. forward (size)
            star(turtle, size /3)
            turtle.left(216)
            turtle.end_fill()
            
star(a, 360)
turtle.done()



#second Graphics

import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(20): #controls the numbers of circle in graphics

    for colours in ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

        turtle.hideturtle()
        
        #MYname is veer singh
