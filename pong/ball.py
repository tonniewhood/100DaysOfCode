# Anthony Wood
# 100 Days of Coding
# Day 22

import turtle as tur

from math import sqrt


class Ball:

    def __init__(self):

        self.ball = tur.Turtle('square')
        self.ball.color('white')
        self.ball.shapesize(stretch_len=0.75, stretch_wid=0.75)

        self.ball.penup()
        self.ball.goto(0, 0)

        self.direction = (1, 0)

    def move(self):
        pos_x = self.ball.pos()[0]
        pos_y = self.ball.pos()[1]

        new_x = pos_x + (self.direction[0] * 10)
        new_y = pos_y + (self.direction[1] * 10)

        self.ball.goto(new_x, new_y)

    def distance(self, thing):
        dx = thing[0] - self.ball.pos()[0]
        dy = thing[1] - self.ball.pos()[1]

        distance = sqrt(dx ** 2 + dy ** 2)

        return distance

    def status_update(self, pad1, pad2):

        # Check to see if the ball has passed the scoring plane either side
        # Then create a vector that details score (x, y) where x indicates
        # that p2 scored, and y indicates p1 scored
        if self.ball.pos()[0] <= -375:
            score = (0, 1)
            self.ball.goto(0, 0)
            self.direction = (-1, 0)
        elif self.ball.pos()[0] >= 370:
            score = (1, 0)
            self.ball.goto(0, 0)
            self.direction = (1, 0)
        else:
            score = (0, 0)
            if self.distance(pad1.body[0].pos()) < 15:
                self.direction = (1, -1)
            elif self.distance(pad1.body[1].pos()) < 15:
                self.direction = (1, 0)
            elif self.distance(pad1.body[2].pos()) < 15:
                self.direction = (1, 1)
            elif self.distance(pad2.body[0].pos()) < 15:
                self.direction = (-1, -1)
            elif self.distance(pad2.body[1].pos()) < 15:
                self.direction = (-1, 0)
            elif self.distance(pad2.body[2].pos()) < 15:
                self.direction = (-1, 1)
            elif self.ball.pos()[1] >= 283:
                self.direction = (self.direction[0], -1)
            elif self.ball.pos()[1] <= -273:
                self.direction = (self.direction[0], 1)

        return score
