from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)


    def bounce(self):
        self.y_move *= -1

    def colision_paddle1(self):
        self.x_move *= -1
        self.ball_speed_up()
        self.move_speed *= 0.8

    def collision_paddle2(self):
        self.x_move *= -1
        self.ball_speed_up()
        self.move_speed *= 0.8


    def reset_position(self):
        self.goto(0,0)

    def ball_speed_up(self):
        pass




