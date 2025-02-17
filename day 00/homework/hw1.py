
from turtle import *
shape("turtle")
width(7)
color("purple")
begin_fill()
for i in range(4):
    forward(200)
    left(90)
forward(70)
end_fill()
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


begin_fill()
penup()
goto(200,200)
pendown()
color("red")
right(150)
forward(200)  
left(120)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(150,140)
pendown()
color("blue")
begin_fill()
for i in range (4):
    forward(30)
    left(90)
end_fill()


penup()
goto(28,140)
pendown()
color("blue")
begin_fill()
for i in range (4):
    forward(30)
    left(90)
end_fill()



exitonclick()