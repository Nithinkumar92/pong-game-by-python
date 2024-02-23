from turtle import Turtle
class Peddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.sco=0
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.up()
        self.goto(pos)


    def up_turtle(self):
            newy = self.ycor() + 20
            self.goto(self.xcor(), newy)

    def down_turtle(self):
            newy = self.ycor() - 20
            self.goto(self.xcor(), newy)
