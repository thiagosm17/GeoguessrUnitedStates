from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.penup()
        self.color("Black")
        self.goto(0, 260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Guess the state {self.points}/50", False, "center", font=('Courier', 24, 'normal'))

    def increase_score(self):
        self.points += 1
        self.update_scoreboard()