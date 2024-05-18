import turtle
import pandas


unitedStatesMap = turtle.Screen()
unitedStatesMap.setup(width=730, height=500)
unitedStatesMap.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

states = pandas.read_csv("50_states.csv")
game_on = True
points = 0

while game_on:
    answer_input = unitedStatesMap.textinput(title="Guess the state", prompt="Guess the state")
    for eachState in states.state:
        if answer_input == eachState:
            points += 1
            print(points)
    if answer_input == "Cancel" or points == 50:
        game_on = False

turtle.mainloop()
