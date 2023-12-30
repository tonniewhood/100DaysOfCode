# Anthony Wood
# 100 Days of Coding
# Day 22

import turtle as tur
import time as t

from paddle import Paddle
from score_board import ScoreBoard
from ball import Ball


def draw_midline():

    midline = tur.Turtle('square')
    midline.color('white')
    midline.penup()
    midline.goto(0, -275)
    midline.setheading(90)
    midline.width(2)

    for i in range(45):
        if i % 2 == 0:
            midline.penup()
            midline.forward(10)
        else:
            midline.pendown()
            midline.forward(15)

    midline.hideturtle()


def make_paddles():
    pad1 = Paddle()
    pad2 = Paddle()

    pad1.move_to(-375, 0)
    pad2.move_to(370, 0)

    return pad1, pad2


def draw_edges():
    pen = tur.Turtle()
    pen.color('white')
    pen.width(3)

    # Draw the bottom line
    pen.penup()
    pen.goto(x=-400, y=-275)
    pen.pendown()
    pen.goto(x=400, y=-275)

    # Draw the top line
    pen.penup()
    pen.goto(x=-400, y=285)
    pen.pendown()
    pen.goto(x=400, y=285)

    # Disable the pen
    pen.hideturtle()


def main():

    # Basic screen setup
    screen = tur.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title('Pong')
    screen.listen()
    screen.onkey(key='Escape', fun=screen.bye)
    screen.tracer(0)

    draw_edges()
    draw_midline()

    # Make the score boards
    score_p1 = 0
    score_p2 = 0
    p1_score_board = ScoreBoard((-130, 215))
    p2_score_board = ScoreBoard((95, 215))

    # Make the ball
    ball = Ball()

    # Create the paddles, and then set up listeners for their movement
    paddle1, paddle2 = make_paddles()
    screen.update()
    screen.onkeypress(key='w', fun=paddle1.move_up)
    screen.onkey(key='s', fun=paddle1.move_down)
    screen.onkey(key='Up', fun=paddle2.move_up)
    screen.onkey(key='Down', fun=paddle2.move_down)

    game_on = True
    winner = 0

    while game_on:

        t.sleep(0.035)
        ball.move()
        score_change = ball.status_update(paddle1, paddle2)
        score_p1 += score_change[0]
        score_p2 += score_change[1]
        p1_score_board.update_score(score_p1)
        p2_score_board.update_score(score_p2)
        if score_p1 == 11 or score_p2 == 11:
            game_on = False
            winner = 1 if score_p1 == 11 else 2

        screen.update()

    end_screen = tur.Turtle()
    end_screen.color('blue')
    end_screen.hideturtle()
    end_screen.penup()
    end_screen.goto(0, -20)
    end_screen.write(arg=f'Player {winner} wins!\n', move=False, align='center', font=('Agency FB', 40, 'normal'))
    screen.update()

    screen.mainloop()
    return 0


main()
