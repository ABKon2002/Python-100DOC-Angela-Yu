from turtle import Turtle
import pandas as pd

FONT = ("Arial", 8, "normal")

class States(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.font_style = FONT
        self.states_df = pd.read_csv("D25 - CSV Data, Pandas Intro\\Data\\50_states.csv")

    def reveal_state(self, state_name):
        if state_name.title() in self.states_df["state"].to_list():
            state_data = self.states_df[self.states_df["state"] == state_name]
            self.goto(state_data["x"].item(), state_data["y"].item())
            self.write(state_data["state"].item(), align = "center", font = self.font_style)
            return True
        else:
            return False
