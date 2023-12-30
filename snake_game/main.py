# Anthony Wood
# 100 Days of Coding
# Day 21

from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time


def draw_border():
    outline = Turtle()
    outline.hideturtle()
    outline.penup()
    outline.goto(x=-360, y=360)
    outline.setheading(0)
    outline.pendown()
    outline.pencolor('white')
    outline.width(3)
    for i in range(4):
        outline.forward(720)
        outline.right(90)


# Initialize the screen setup
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor('#000000')
screen.title('Le Snake Game')
screen.tracer(0)

# Initialize the snake as well as the food
snake = Snake()
food = Food(snake.snake_body)

# Initialize the score board
score_board = Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(0, 365)
score_board.color('white')
score = 0
score_board.write(arg=f'Score: {score}', move=False, align='center', font=('Rockwell', 20, 'normal'))

# Enable all the event listeners to allow movement of the snake in the game
screen.listen()

screen.onkey(key='Up', fun=snake.go_up)
screen.onkey(key='Down', fun=snake.go_down)
screen.onkey(key='Left', fun=snake.go_left)
screen.onkey(key='Right', fun=snake.go_right)
screen.update()

# Draw the outer border of the game
draw_border()


game_is_on = True

while game_is_on:
    # Pause long enough so the animation shows, then move the snake, update its position, and make determine
    # if the game should end or not. Also print the score to the screen
    time.sleep(0.1)
    snake.move_snake()
    game_is_on, score = snake.update(food, score)
    screen.update()
    score_board.clear()
    score_board.write(arg=f'Score: {score}', move=False, align='center', font=('Rockwell', 20, 'normal'))

# Print the game over screen, and allow esc to exit
game_over = Turtle()
game_over.hideturtle()
game_over.color('white')
game_over.write(arg="Game Over.\n", align='center', move=False, font=('Rockwell', 45, 'normal'))
game_over.write(arg="Press escape to exit.", align='center', move=False, font=('Rockwell', 20, 'normal'))
screen.onkey(key='Escape', fun=screen.bye)

screen.mainloop()
