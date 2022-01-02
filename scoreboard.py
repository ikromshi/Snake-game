from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
ABORT = "GAME OVER"
ABORT_FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def abort(self):
        self.goto(0, 0)
        self.write(ABORT, align=ALIGNMENT,  font=ABORT_FONT)
