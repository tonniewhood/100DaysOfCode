
import pandas
import turtle as tur


# Create the screen for the game/quiz
screen = tur.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)

# Create the turtle that has the image
bg = tur.Turtle(image)
state_name = tur.Turtle()
state_name.hideturtle()
state_name.penup()

# Read the CSV in
states = pandas.read_csv("50_states.csv")

game_on = True
won = False
prompt = "Guess a state"
guessed = []
score = 0
score_tur = tur.Turtle()
score_tur.penup()
score_tur.hideturtle()
score_tur.goto(-250, 250)
score_tur.write(f"Score: {score}")

while game_on:

    guess = screen.textinput(title="Guess time", prompt=prompt)

    if guess is None or guess == "exit":
        game_on = False
    else:
        guess = guess.title()

    guess_row = states[states.state == guess]

    if len(guess_row) == 1 and guessed.count(guess) < 1:
        prompt = "Guess a state"
        guessed.append(guess)
        score += 1
        x_coord = guess_row.x.iloc[0]
        y_coord = guess_row.y.iloc[0]
        state_name.goto(x_coord, y_coord)
        state_name.write(guess)
    elif guessed.count(guess) > 0:
        prompt = "Pick a new state"
    else:
        prompt = f"No state named {guess}\nGuess a state"

    score_tur.clear()
    score_tur.write(f"Score: {score}")

    if len(guessed) == 50:
        game_on = False
        won = True

screen.listen()
screen.onkey(key="Escape", fun=screen.bye)

screen.mainloop()
