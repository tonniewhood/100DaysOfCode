# Anthony Wood
# 100 Days of Coding
# Day 21

from turtle import Turtle
from math import sqrt


class SnakeNode:

    def __init__(self, starting_coordinates):
        self.node = Turtle('square')
        self.node.penup()
        self.node.color('white')
        self.node.goto(starting_coordinates)
        self.position = starting_coordinates

    def go_to(self, coordinates):
        self.node.goto(coordinates)
        self.position = coordinates

    # Determine the distance of any node to the head
    def distance(self, head):
        node_x = self.position[0]
        node_y = self.position[1]
        head_x = head.position[0]
        head_y = head.position[1]
        leg_1 = node_y - head_y
        leg_2 = node_x - head_x
        hypotenuse = sqrt(leg_1 ** 2 + leg_2 ** 2)
        return hypotenuse
