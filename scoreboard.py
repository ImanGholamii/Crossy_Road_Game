from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("#66CDAA")
        self.teleport(-300, 260)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.setpos(-80, 0)
        self.write(f"Game Over", font=FONT)

    def add_level(self):
        self.level += 1
        self.update_board()

    def reset(self):
        self.clear()
        self.level = 1
        self.goto(-300, 260)
        self.update_board()
