# Anthony Wood
# 100 Days of Coding
# Day 21

import turtle as tur


class Paddle:

    def __init__(self):
        self.body = []
        for i in range(3):
            self.body.append(tur.Turtle('square'))
            self.body[i].color('white')
            self.body[i].penup()

    def move_to(self, x, y):

        for i in range(len(self.body)):

            new_y = y + ((i - 1) * 20)
            self.body[i].goto(x, new_y)

    def move_up(self):

        for body_part in self.body:
            body_part.setheading(90)
            body_part.forward(30)

    def move_down(self):

        for body_part in self.body:
            body_part.setheading(-90)
            body_part.forward(30)
