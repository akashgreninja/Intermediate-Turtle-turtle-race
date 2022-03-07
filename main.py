import random
import turtle
from turtle import Turtle,Screen


colors=["yellow","red","green","blue","grey"]



screen=Screen()
screen.setup(width=500,height=400)
user_guess=screen.textinput("Which color?","Which color will win?")
# print(user_guess)

all_turtles=[]

turtle_positions=[-80,-40,0,40,80]
for i in range (5):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])

    turtle.penup()
    turtle.goto(x=-230,y=turtle_positions[i])
    all_turtles.append(turtle)

#
# if user_guess:
#     race_on=True
race_on=True

while race_on:
    for tur in all_turtles:
        if tur.xcor()>230:
            race_on =False
            winning_color=tur.pencolor()
            if winning_color==user_guess:

                print(f"you won ,{winning_color} is the winner")
            # elif len(winning_color)>2:
            #     print("its a draw between 2 turtles ")
            else:
                print(f"you loose{winning_color} won !! LMAO")



    for m in range(0,5):
        alpha=all_turtles[m]
        alpha.forward(random.randint(0,20))

        # alpha.speed(random.randint(0,10))








# turtle2=Turtle()


# alpha=-10
# beta=-300







#
#
#
# for i in range (1):
#
#     turtle.shape("turtle")
#     turtle.color(random.choice(colors))
#     turtle.penup()
#
#     turtle.goto(beta,alpha)
#
# for i in range (1):
#
#     turtle2.shape("turtle")
#     turtle2.color(random.choice(colors))
#     turtle2.penup()
#
#     turtle2.goto(-320,10)
#
#
#
# for n in range (20):
#     turtle.forward(20)
#     turtle.speed(random.choice(speeds))



screen.exitonclick()