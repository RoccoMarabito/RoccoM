import turtle


t = turtle.Turtle()
t2 = turtle.Turtle()
t2.hideturtle()
t2.penup()
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor('light Green')


t.write("What I like", font=("Arial", 30, "bold"), align="center")
t.penup()
t.goto(0,-50)
t.write(" By Rocco", font=("Arial", 30, "bold"), align="center")
enter = input("Enter to begin")
# end of first screen
screen.bgcolor('orange')
t.clear()
t2.clear()

# second screen begin

t2.goto(-150,100)

turtle.addshape("steak.gif")
t2.shape("steak.gif")
a = t2.stamp()
t2.goto(-150,100)

t2.goto(150,100)
turtle.addshape("Chicken.gif")
t2.shape("Chicken.gif")
a = t2.stamp()
t2.goto(150,100)

t2.goto(150,200)
turtle.addshape("Alfredo.gif")
t2.shape("Alfredo.gif")
a = t2.stamp()



t.penup()
t.goto(0,-50)
t.write("Favorite Foods",font=("arial",20,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-100)
t.write("steak",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-150)
t.write("Chicken Fingers",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-200)
t.write("Chicken Alfredo",font=("arial",15,'bold'),align="center")
t.penup()


# end of screen 2

enter = input("Enter to begin")
screen.bgcolor('cornflower blue')
t.clear()
t2.clear()
# start of screen 3

t.penup()
t.goto(-300,100)
t.pendown()
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)

t2.goto(150,200)
turtle.addshape("spider.gif")
t2.shape("spider.gif")
a = t2.stamp()

t.penup()
t.goto(0,100)
t.write("My favorite Movie", font=("Arial", 20, "bold"), align="center")
t.penup()
t.goto(0,0)
t.write(" The Amazing Spider-man", font=("Arial", 20, "bold"), align="center")
# end of screen 3

enter = input("Enter to begin")
screen.bgcolor("red")

t.clear()
t2.clear()
# start of screen 4

t2.goto(150,200)
turtle.addshape("Mj.gif")
t2.shape("Mj.gif")
a = t2.stamp()


t.write("My favorite Sport", font=("Arial", 20, "bold"), align="center")
t.penup()
t.goto(100,-50)
t.write("Basketball is my favorite sport ", font=("Arial", 10, "bold"), align="center")
t.goto(-300,100)
t.pendown()
t.begin_fill()
t.fillcolor('orange')
t.circle(50)
t.end_fill()
# end of screen 4
enter = input("Enter to begin")
screen.bgcolor("hot pink")
t.clear()
t2.clear()

# start of screen 5
t2.goto(-150,100)

turtle.addshape("music.gif")
t2.shape("music.gif")
a = t2.stamp()
t2.goto(-150,100)

t2.goto(150,100)
turtle.addshape("gaming.gif")
t2.shape("gaming.gif")
a = t2.stamp()
t2.goto(150,100)

t2.goto(150,200)
turtle.addshape("lifting.gif")
t2.shape("lifting.gif")
a = t2.stamp()
t2.goto(150,200)
t2.goto(-150,200)
turtle.addshape("sleep.gif")
t2.shape("sleep.gif")
a = t2.stamp()
t2.goto(-150,200)



t.penup()
t.goto(0,-50)
t.write("Favorite Hobbies",font=("arial",20,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-100)
t.write("sleeping",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-150)
t.write("lifting weights",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-200)
t.write("Listening to music",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-250)
t.write("Gaming",font=("arial",15,'bold'),align="center")
t.penup()

#octagon
t.fillcolor('yellow')
t.begin_fill()
t.penup()
t.goto(-25,100)
t.pendown()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.end_fill()
turtle.done()