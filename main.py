import time
from turtle import Turtle,Screen
from peddle import Peddle
from ball import Ball
from score import Score

screen=Screen()

screen.bgcolor("Black")
screen.setup(800,600)
screen.title("pong")
screen.tracer(0)
l_pos=(-350,0)
r_pos=(350,0)
tom=Peddle(l_pos)
tom2=Peddle(r_pos)
ball=Ball()
screen.listen()

screen.onkey(tom.up_turtle,"w")
screen.onkey(tom.down_turtle,"s")

screen.onkey(tom2.up_turtle,"Up")
screen.onkey(tom2.down_turtle,"Down")
score=Score()
game=True
while game:
    screen.update()
    time.sleep(ball.speed_of)
    ball.move()
    if ball.ycor()>285 or ball.ycor() < -280:
        ball.y_move()
    if ball.distance(tom2)<50 and ball.xcor()>320:
        ball.x_move()
    if ball.distance(tom)<50 and ball.xcor()<-320:
        ball.x_move()
    if ball.xcor()>380 :
        ball.miss()
        score.leftscore()
        score.scoreboard()
    if ball.xcor()<-380:
        ball.miss()
        score.rightscore()
        score.scoreboard()

screen.exitonclick()