import turtle
import pandas
from state import State


unitedStatesMap = turtle.Screen()
unitedStatesMap.setup(width=730, height=500)
unitedStatesMap.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

states = pandas.read_csv("50_states.csv")
game_on = True
points = 0
correctGuesses = []

while game_on:
    user_answer = unitedStatesMap.textinput(title=f"Guess the state {points}/50", prompt="Guess the state")
    current_guess = State(states, user_answer, correctGuesses)
    if current_guess.check_if_the_guess_is_correct():
        current_guess.write_current_guess()
        correctGuesses.append(user_answer)
        points += 1

    if user_answer == "Cancel" or points >= 50:
        game_on = False

turtle.mainloop()


