# Pong Game

import turtle

import random as rand
wall_barrier1 = (451,0)
wall_barrier2 = (-451,0)
wn = turtle.Screen()
turtle.Screen().bgcolor('black')
font_setup = ("Roboto" ,50, "normal")
wn.screensize(1,1)
turtle.penup()
turtle.shapesize(1)
turtle.speed("slowest")
turtle.shape("square")
turtle.color("white")

'''

    

while turtle touch wall = False:
    turtle.goto(rand.randint(0,-300),rand.randint(0,300))
'''
paddle_image = "paddle1.gif"
paddle = turtle.Turtle()
paddle.hideturtle()
wn.addshape(paddle_image)

'''
def draw_paddle():
'''



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



def update_player_1_score():
    '''
    if ball touch_wall:
    score.clear()
    score += 1
    print(score)
    '''

def update_player_2_score():
    '''
    if ball touch_wall:
    score2.clear()
    score2 += 1
    print(score2)
    '''

letter_w = "w"
letter_s = "s"
letter_i = "i"
letter_k = "k"




'''
wn.onkeypress(letter_w, w)
wn.onkeypress(letter_s, s)
wn.onkeypress(letter_i, "Up")
wn.onkeypress(letter_k, "Down")
'''
wn.listen()
wn.mainloop()