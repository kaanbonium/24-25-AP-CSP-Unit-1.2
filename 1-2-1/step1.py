# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = 'circle'
font_setup = ("Arial", 20, "normal")
colors = ["red", "blue", "green", "yellow"]
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
#visually shows the score count
score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-375, 275)
score_writer.pendown()
#the timer
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#countdown variable
counter =  trtl.Turtle()
counter.speed(0)
counter.hideturtle()
counter.penup()
counter.goto(-375, 300)
counter.pendown()
#-----game functions--------

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
score = 0
def update_score():
    global score
    score += 1
    score_writer.clear()
    print(score_writer.write(score, font=font_setup))



def change_position():
    spot.speed(0)
    new_xpos = rand.randint(0, 400)
    new_ypos = rand.randint(0, 300)
    spot.penup()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()

def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        update_score()
        change_position()

    else:
        spot.hideturtle()



#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor('gray')
wn.ontimer(countdown, counter_interval)
wn.mainloop()