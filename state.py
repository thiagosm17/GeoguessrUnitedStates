import turtle


class State(turtle.Turtle):
    def __init__(self, states, answer_input, correctGuesses):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.states = states
        self.correctGuesses = correctGuesses
        self.answer_input = answer_input

    def is_it_already_guessed(self):
        for guesses in self.correctGuesses:
            if self.answer_input.lower() == guesses.lower():
                return True
        return False

    def check_if_the_guess_is_correct(self):
        for eachState in self.states.state:
            if self.answer_input.lower() == eachState.lower() and not (self.is_it_already_guessed()):
                return True
        return False

    def write_current_guess(self):
        location = self.states[self.states["state"] == self.answer_input]
        self.goto(x=int(location.x), y=int(location.y))
        self.write(self.answer_input)
