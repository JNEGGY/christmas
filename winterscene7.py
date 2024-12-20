import turtle


screen=turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("lightsteelblue")
t=turtle.Turtle()

t_ground=turtle.Turtle()
t_ground.penup()
t_ground.pencolor("snow1")
t_ground.fillcolor("snow1")
t.pensize(50)
t_ground.speed(0)
t_ground.begin_fill()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

window=turtle.Screen()
t=turtle.Turtle()
s=t.getscreen()
s.bgcolor('lightblue')

t.color('green')
t.pensize(5)
t.begin_fill()

t.forward(100)
t.left(150)
t.forward(90)
t.right(150)
t.forward(60)
t.left(150)
t.forward(60)
t.right(150)
t.forward(40)
t.left(150)
t.forward(100)
t.end_fill()

t.begin_fill()
t.left(60)
t.forward(100)
t.left(150)
t.forward(40)
t.right(150)
t.forward(60)
t.left(150)
t.forward(60)
t.right(150)
t.forward(90)
t.left(150)
t.forward(133)
t.end_fill()

t.pencolor('chocolate')
t.pensize(1)
t.fillcolor("chocolate")
t.begin_fill()
t.right(90)
t.forward(80)
t.right(90)
t.forward(40)
t.right(90)
t.forward(80)
t.end_fill()

t.penup()
t.color('purple')
t.goto(110,-10)
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.color('blue')
t.goto(-120,-10)
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.color('navy')
t.goto(100,40)
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.color('red')
t.goto(-105,38)
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.color('orange')
t.goto(85,70)
t.begin_fill()
t.circle(7)
t.end_fill()

t.penup()
t.color('yellow')
t.goto(-95,70)
t.begin_fill()
t.circle(7)
t.end_fill()

t.shape('triangle')
t.fillcolor('pink')
t.goto(-20,30)
t.setheading(90)
t.stamp()
t.fillcolor('lightblue')
t.goto(20,60)
t.setheading(90)
t.stamp()
t.goto(-40,75)
t.setheading(90)
t.stamp()

t.speed(5)
t.penup()
t.color('yellow')
t.goto(-20,110)
t.begin_fill()
t.pendown()

t.penup()


message="It's The Season To Be Jolly!"
t.goto(0,200)
t.color('red')
t.write(message,move=False,align='center',font=('Arilal',20,'bold'))

t.penup()

t.fillcolor("gold")
t.begin_fill()
t.pendown()
t.goto(-400,400)
t.circle(100)
t.pendown()
t.end_fill()
t.pendown()

t_present = turtle.Turtle()
t_present.hideturtle()
t_present.speed(0)
t_present.penup()
t_present.goto(-65,-100)
t_present.pendown()
t_present.fillcolor("pink")
t_present.begin_fill()
t_present.forward(50)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.end_fill()
t_present.penup()
t_present.goto(-40,-100)
t_present.pendown()
t_present.fillcolor("teal")
t_present.begin_fill()
t_present.forward(5)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(5)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.end_fill()
t_present.penup()
t_present.goto(-65,-75)
t_present.pendown()
t_present.fillcolor("teal")
t_present.begin_fill()
t_present.forward(50)
t_present.left(90)
t_present.forward(5)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(5)
t_present.left(90)
t_present.end_fill()

t_present = turtle.Turtle()
t_present.hideturtle()
t_present.speed(0)
t_present.penup()
t_present.goto(-150,-100)
t_present.pendown()
t_present.fillcolor("red")
t_present.begin_fill()
t_present.forward(50)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.end_fill()
t_present.penup()
t_present.goto(-135,-100)
t_present.pendown()
t_present.fillcolor("green")
t_present.begin_fill()
t_present.forward(5)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(5)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.end_fill()
t_present.penup()
t_present.goto(-150,-75)
t_present.pendown()
t_present.fillcolor("green")
t_present.begin_fill()
t_present.forward(50)
t_present.left(90)
t_present.forward(5)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(5)
t_present.left(90)
t_present.end_fill()



#this is the last line of code
turtle.done()