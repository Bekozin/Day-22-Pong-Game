import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle((350,0))

paddle2 = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up,"Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up,"w")
screen.onkey(paddle2.go_down,"s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 300 or ball.ycor() < -300 :
        ball.bounce()

    elif ball.xcor() >= 340 and ball.distance(paddle1) <= 50:
        ball.colision_paddle1()

    elif ball.xcor() <= -340 and ball.distance(paddle2) <= 50:
        ball.collision_paddle2()

    elif ball.xcor() > 380:
        ball.reset_position()
        time.sleep(1)
        scoreboard.paddle2_point()

    elif ball.xcor() < - 380:
        ball.reset_position()
        time.sleep(1)
        scoreboard.paddle1_point()

































screen.exitonclick()