from turtle import Turtle
SCORE_FONT = ("Courier", 24, "normal")
SCORE_COLOR = "white"
GAME_OVER_FONT = ("Courier", 24, "normal")
GAME_OVER_COLOR = "red"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        with open('D21 - The-snake-game-final\high_score.txt', 'r') as f:
            self.previous_high_score = int(f.read())
        self.high_score = self.previous_high_score
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}", align = "center", font = SCORE_FONT)

    # def prompt_retry(self):
    #     self.goto(0, 0)
    #     self.color(SCORE_COLOR)
    #     self.write("Press 'p' to play again", align = "center", font = SCORE_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            if self.high_score > self.previous_high_score:
                with open('D21 - The-snake-game-final\high_score.txt', 'w') as f:
                    f.write(str(self.high_score))
                    self.previous_high_score = self.high_score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color(GAME_OVER_COLOR)
    #     self.write("GAME OVER !", align = "center", font = GAME_OVER_FONT)

    def ding_ding(self):
        self.score += 1
        self.update_scoreboard()
