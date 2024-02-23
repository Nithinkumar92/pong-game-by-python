from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.up()
        self.x_value=10
        self.y_value=10
        self.speed_of=0.1
    def move(self):
        new_x=self.xcor()+self.x_value
        new_y=self.ycor()+self.y_value
        self.goto(new_x,new_y)

    def y_move(self):
        self.y_value*=-1

    def x_move(self):
        self.x_value*=-1
        self.speed_of*=0.9

    def miss(self):
        self.goto(0,0)
        self.x_move()
        self.speed_of=0.1



