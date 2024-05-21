from turtle import Turtle
import heroes

timmy = Turtle()
timmy.home()

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

timmy.pos()
print(heroes.gen())

# initial thought process
for steps in range(100):
    for color in ('black','white'):
        timmy.color(color)
        timmy.forward(10)

# utilization of library methods
for steps in range(100):
    timmy.forward(10)
    timmy.pu()
    timmy.forward(10)
    timmy.pd()

timmy.pos()
