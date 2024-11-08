from turtle import Turtle
SCORE_FONT = ("Courier", 24, "normal")
SCORE_COLOR = "white"
GAME_OVER_FONT = ("Courier", 24, "normal")
GAME_OVER_COLOR = "red"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.right_score} : {self.left_score}", align = "center", font = SCORE_FONT)

    def check_game_over(self):
        if self.right_score == 5 or self.left_score == 5:
            self.game_over()
            return False
        return True

    def game_over(self):
        self.goto(0, 0)
        self.color(GAME_OVER_COLOR)
        if self.right_score == 5:
            self.write("RIGHT PLAYER WINS !", align = "center", font = GAME_OVER_FONT)
        else:
            self.write("LEFT PLAYER WINS !", align = "center", font = GAME_OVER_FONT)

    def ding_ding_left(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()
        return self.check_game_over()

    def ding_ding_right(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()
        return self.check_game_over()