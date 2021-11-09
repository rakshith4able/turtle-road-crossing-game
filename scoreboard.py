FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-240, 270)
        self.update_level_text()

    def update_level_text(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_level_text()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Courier", 15, "normal"))
