# Anthony Wood
# 100 Days of Coding
# Day 21

from snake_node import SnakeNode


class Snake:

    # Create the list of snake_nodes
    def __init__(self):
        self.snake_body = []
        for i in range(3):
            coordinates = (i * -20, 0)
            self.snake_body.append(SnakeNode(coordinates))

    # Grow the snake by tacking it onto the end of the snake in line with the final two nodes
    def grow(self):
        last_idx = len(self.snake_body) - 1
        last = self.snake_body[last_idx]
        second_last = self.snake_body[last_idx - 1]

        x_diff = second_last.position[0] - last.position[0]
        y_diff = second_last.position[1] - last.position[1]

        new_x = last.position[0] - x_diff
        new_y = last.position[1] - y_diff
        new_coordinates = (new_x, new_y)
        self.snake_body.append(SnakeNode(new_coordinates))

    def move_snake(self):
        head = self.snake_body[0]

        # Move the head of the snake forward, and then set the head's position as the position of the next node to go to
        head_x = int(head.node.pos()[0])
        head_y = int(head.node.pos()[1])
        next_node_coordinates = (head_x, head_y)
        head.node.forward(20)
        head_x = int(head.node.pos()[0])
        head_y = int(head.node.pos()[1])
        head.position = (head_x, head_y)

        # For all elements in the snake, move them to the position of the node that was next closest to the head
        for i in range(1, len(self.snake_body)):
            current_position = self.snake_body[i].position
            self.snake_body[i].go_to(next_node_coordinates)
            next_node_coordinates = current_position

    # Check to make sure that there is no node above the snake before setting to move in that direction
    def go_up(self):
        head = self.snake_body[0]
        right_after_head = self.snake_body[1]
        if right_after_head.position[1] < head.position[1] + 20:
            head.node.setheading(90)

    # Check to make sure that there is no node below the snake before setting to move in that direction
    def go_down(self):
        head = self.snake_body[0]
        right_after_head = self.snake_body[1]
        if right_after_head.position[1] > head.position[1] - 20:
            head.node.setheading(270)

    # Check to make sure that there is no node to the left the snake before setting to move in that direction
    def go_left(self):
        head = self.snake_body[0]
        right_after_head = self.snake_body[1]
        if right_after_head.position[0] > head.position[0] - 20:
            head.node.setheading(180)

    # Check to make sure that there is no node to the right the snake before setting to move in that direction
    def go_right(self):
        head = self.snake_body[0]
        right_after_head = self.snake_body[1]
        if right_after_head.position[0] < head.position[0] + 20:
            head.node.setheading(0)

    def update(self, food, score):
        head = self.snake_body[0]

        # Check to make sure that the head is between the borders of the screen
        if (-360.0 < head.position[0] < 360) and (-360.0 < head.position[1] < 360):
            for i in range(1, len(self.snake_body)):
                distance = self.snake_body[i].distance(head)
                # Determine the distance to all node in the body, and determine if the game should end
                if distance < 15:
                    return False, score

            # Determine the distance from the head to the food, and decide if the snake should grow
            if food.distance(head) < 15:
                self.grow()
                score += 1
                food.change_position(self.snake_body)

            return True, score

        else:
            return False, score
