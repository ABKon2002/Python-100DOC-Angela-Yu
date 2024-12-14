from turtle import Turtle

SCORE_FONT = ("Courier", 20, "normal")
SCORE_COLOR = "white"
HEADING_FONT = ("Courier", 24, "bold")
HEADING_COLOR = 'white'
TEXT_FONT = ("Courier", 16, "normal")
TEXT_COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.strikes = 3
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(-220, 250)
        self.hideturtle()
        self.display_heading_here()
    
    def display_heading_here(self):
        self.penup()
        self.goto(0, 250)
        self.color(HEADING_COLOR)
        self.write("US States Game", align= 'center', font = HEADING_FONT)
        self.write("You have 3 strikes, guess 50 states.",
                   align = 'center', font = TEXT_FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    Strikes: {self.strikes}", align = "center", font = SCORE_FONT)
        self.check_game_over()
    
    def striked(self):
        self.strikes -= 1
        self.update_scoreboard()
    
    def check_game_over(self):
        if self.strikes <= 0:
            self.game_over()

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER !", align = "center", font = HEADING_FONT)

    def ding_ding(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
