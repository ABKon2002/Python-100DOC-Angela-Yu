from turtle import Turtle

SCORE_FONT = ("Courier", 24, "normal")
SCORE_COLOR = "white"
GAME_OVER_FONT = ("Courier", 24, "normal")
GAME_OVER_COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(-220, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = "center", font = SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color(GAME_OVER_COLOR)
        self.write("GAME OVER !", align = "center", font = GAME_OVER_FONT)

    def increase_level(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
