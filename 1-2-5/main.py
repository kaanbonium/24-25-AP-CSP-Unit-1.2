import turtle

# Setup game window
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=900, height=690)
wn.tracer(0)
font_setup = ("Arial", 24, "normal")

# paddle 1
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=.9)
paddle_a.penup()
paddle_a.goto(-400, 0)

# paddle 2
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=.9)
paddle_b.penup()
paddle_b.goto(400, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball_speed_x = .30  # Speed remains constant
ball_speed_y = .30  # Speed remains constant
ball.color("red")

# scores
score_a = 0
score_b = 0

# Display scores
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 300)
score_display.write("Player A: 0  Player B: 0", align="center", font=font_setup)

# Update score display
def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=font_setup)

# Move paddle a up
def paddle_a_up():
    if paddle_a.ycor() < 300:
        paddle_a.sety(paddle_a.ycor() + 30)

# Move paddle a down
def paddle_a_down():
    if paddle_a.ycor() > -300:
        paddle_a.sety(paddle_a.ycor() - 30)

# Move paddle b up
def paddle_b_up():
    if paddle_b.ycor() < 300:
        paddle_b.sety(paddle_b.ycor() + 30)

# Move paddle b down
def paddle_b_down():
    if paddle_b.ycor() > -300:
        paddle_b.sety(paddle_b.ycor() - 30)

# controls
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")

# Main game loop
while True:
    wn.update()
    # Move ball
    ball.setx(ball.xcor() + ball_speed_x)
    ball.sety(ball.ycor() + ball_speed_y)

    # Ball bounce off paddles
    if (ball.xcor() > 380 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball_speed_x *= -1 # Speed of ball gets reflected
    if (ball.xcor() < -380 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball_speed_x *= -1 # Reflected again

    # Ball bounces top and bottom walls
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball_speed_y *= -1

    # If ball goes out of bounds
    if ball.xcor() > 450:
        ball.goto(0, 0)
        ball_speed_x *= -1
        score_a += 1
        update_score()

    if ball.xcor() < -450:
        ball.goto(0, 0)
        ball_speed_x *= -1
        score_b += 1
        update_score()