from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.hideturtle()
        self.penup()
        self.color("#66CDAA")
        self.teleport(-300, 260)
        self.write(f"Level: {self.point}", font=FONT)

    def game_over(self):
        self.setpos(-80, 0)
        self.write(f"Game Over", font=FONT)
