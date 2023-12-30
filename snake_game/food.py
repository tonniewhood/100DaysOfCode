# Anthony Wood
# 100 Days of Coding
# Day 21

from random import randrange
from turtle import Turtle
from math import sqrt


class Food:

    def __init__(self, snake_body):
        self.food = Turtle('circle')
        self.food.color('blue')
        self.position = (0, 0)
        self.change_position(snake_body)

    def change_position(self, snake_body):
        position_ok = False

        while not position_ok:
            x_pos = randrange(-340, 340, 20)
            y_pos = randrange(-340, 340, 20)
            attempted_position = (x_pos, y_pos)

            # Verify that for all positions in the snake, the food is not going to the same place as the body
            # If it's fine to go there, put the food there
            for snake_node in snake_body:
                if attempted_position != snake_node.position:
                    self.position = attempted_position
                    self.food.penup()
                    self.food.goto(attempted_position)
                    position_ok = True

    # This determines the distances from any node (though usually the head) using the pythagorean theorem
    def distance(self, head):
        food_x = self.position[0]
        food_y = self.position[1]
        head_x = head.position[0]
        head_y = head.position[1]
        leg_1 = food_y - head_y
        leg_2 = food_x - head_x
        hypotenuse = sqrt(leg_1 ** 2 + leg_2 ** 2)
        return hypotenuse
