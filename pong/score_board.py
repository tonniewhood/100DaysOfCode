# Anthony Wood
# 100 Days of Coding
# Day 22

import turtle as tur
import scores as s


class ScoreBoard:

    def __init__(self, coordinates):
        self.segments = []
        def_score = s.scores[0]

        mid_x = coordinates[0]
        mid_y = coordinates[1]

        for i in range(26):
            to_add = tur.Turtle('square')
            self.segments.append(to_add)
            self.segments[i].color('white')
            self.segments[i].penup()
            if def_score[i] == 0:
                self.segments[i].hideturtle()

            seg_x = 0
            seg_y = 0

            if s.x_1.count(i) == 1:
                seg_x = mid_x - 60
            elif s.x_2.count(i) == 1:
                seg_x = mid_x - 40
            elif s.x_3.count(i) == 1:
                seg_x = mid_x - 20
            elif s.x_4.count(i) == 1:
                seg_x = mid_x + 20
            elif s.x_5.count(i) == 1:
                seg_x = mid_x + 40
            elif s.x_6.count(i) == 1:
                seg_x = mid_x + 60

            if s.y_1.count(i) == 1:
                seg_y = mid_y + 40
            elif s.y_2.count(i) == 1:
                seg_y = mid_y + 20
            elif s.y_3.count(i) == 1:
                seg_y = mid_y
            elif s.y_4.count(i) == 1:
                seg_y = mid_y - 20
            elif s.y_5.count(i) == 1:
                seg_y = mid_y - 40

            self.segments[i].goto(seg_x, seg_y)

    def update_score(self, new_score):
        new_score_list = s.scores[new_score]
        for i in range(len(self.segments)):
            if new_score_list[i] == 1:
                self.segments[i].showturtle()
            else:
                self.segments[i].hideturtle()
