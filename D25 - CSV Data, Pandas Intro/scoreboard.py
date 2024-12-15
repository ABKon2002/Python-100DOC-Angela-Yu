from turtle import Turtle

SCORE_FONT = ("Courier", 20, "normal")
SCORE_COLOR = "white"
HEADING_FONT = ("Courier", 24, "bold")
HEADING_COLOR = 'white'
TEXT_FONT = ("Courier", 16, "normal")
TEXT_COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self, map = 'US'):
        super().__init__()
        self.score = 0
        self.strikes = 3
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(-220, 250)
        self.hideturtle()
        if map == 'US':
            self.display_heading_US()
        elif map == 'IND':
            self.display_heading_IND()
    
    def display_heading_US(self):
        self.penup()
        self.goto(0, 370)
        self.color('black')
        self.write("US States Game", align= 'center', font = HEADING_FONT)
        self.write("You have 3 strikes, guess 50 states.",
                   align = 'center', font = TEXT_FONT)
    
    def display_heading_IND(self):
        self.penup()
        self.goto(0, 250)
        self.color(HEADING_COLOR)
        self.write("India States Game", align= 'center', font = HEADING_FONT)
        self.write("You have 3 strikes, guess 29 states.",
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
