#IMPORTS
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

#WINDOW SETUP
window = Screen()
window.setup(1000, 600)
window.bgcolor('black')
window.title('Ping Pong !')
window.tracer(0)

#OBJECTS SETUP
r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
ball = Ball()
score = Score()

def make_game_false():
    global game
    game = False
    
#WINDOW LISTENING
window.listen()
window.onkey(r_paddle.up, "Up")
window.onkey(r_paddle.down, "Down")
window.onkey(l_paddle.up, "w")
window.onkey(l_paddle.down, "s")
window.onkey(make_game_false, "Escape")

#MAIN GAME
speed = 0.1
game = True
while game:
    window.update()
    time.sleep(speed)
    
    ball.goto(ball.xcor()+ball.x, ball.ycor()+ball.y)
    
    #IF BALL TOUCHED Y AXIS
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y *= -1
        
    #IF BALL TOUCHED PADDLE
    if (ball.xcor() >= 430 and ball.distance(r_paddle) <= 50) or (ball.xcor() <= -430 and ball.distance(l_paddle) <= 50):
        ball.x *= -1
        speed *= 0.8
        
    #IF LEFT PADDLE SCORED A GOAL
    if ball.xcor() > 500:
        score.l_point()
        ball.goto(0,0)
        ball.x *= -1
        speed = 0.1
        
    #IF WRITE PADDLE SCORED A GOAL
    if ball.xcor() < -500:
        score.r_point()
        ball.goto(0,0)
        ball.x *= -1
        speed = 0.1

window.exitonclick()