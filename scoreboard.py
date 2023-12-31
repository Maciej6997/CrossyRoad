from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        """
        Function updates scoreboard
        """
        self.clear()
        self.goto(-200,250)
        self.write(f'Level {self.score}', align='center', font=FONT)

    def take_point(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)
