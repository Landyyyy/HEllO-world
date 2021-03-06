
import turtle

wn = turtle.Screen()
wn.title("Pong by xl")
wn.bgcolor("grey")
wn.setup(width=1000, height=600)
wn.tracer(0)  # stop the window updated

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid=10, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("pink")
paddle_b.shapesize(stretch_wid=10, stretch_len=1)
paddle_b.penup()
paddle_b.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("darkslategray1")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Times", 24, "bold"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 15
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 15
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 15
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 15
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Times", 24, "bold"))

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Times", 24, "bold"))

    # Paddle and ball collisions
    if (450 > ball.xcor() > 440) and (paddle_b.ycor() + 120 > ball.ycor() > paddle_b.ycor() - 120):
        ball.setx(440)
        ball.dx *= -1
    if (-440 > ball.xcor() > -450) and (paddle_a.ycor() + 120 > ball.ycor() > paddle_a.ycor() - 120):
        ball.setx(-440)
        ball.dx *= -1