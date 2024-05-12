from turtle import *
width(5)
#body
color("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()


penup()
goto(200,200)
pendown()

#roof
color("orange")
begin_fill()
right(90)
right(45)
forward(141)
left(90)
forward(141)
end_fill()



color("red")
left(45)
forward(200)
left(90)
forward(75)


#door
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

penup()
goto(20,180)
pendown()

#window1
color("black")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(180,180)
pendown()
#window2
color("black")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()