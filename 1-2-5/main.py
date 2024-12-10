# Pong Game

import turtle
import random as rand
wn = turtle.Screen()
turtle.Screen().bgcolor('black')
font_setup = ("Roboto" ,50, "normal")

turtle.penup()
turtle.shape("circle")
turtle.color("white")
turtle.shapesize(1)
turtle.goto(100,100)





score = turtle.Turtle()
score.hideturtle()
score.speed(0)
score.color('white')
score.penup()
score.goto(200, 312)
score.write("0", font=font_setup)
score2 = turtle.Turtle()
score2.hideturtle()
score2.speed(0)
score2.color('white')
score2.penup()
score2.goto(-200, 312)
score2.pendown()
score2.write("0", font=font_setup)



def player_1_score():
    '''
    if ball goes into zone:
    score.clear()
    score += 1
    print(score)
    '''

def player_2_score():
    '''
    if ball goes into zone:
    score2.clear()
    score2 += 1
    print(score2)
    '''





























wn.on
wn.mainloop()