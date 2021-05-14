from turtle import Turtle

ALLIGNMENT = "center"
FONT_STYLE_1 = ("Times New Roman", 24, "bold")
FONT_STYLE_2 = ("Times New Roman", 14, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALLIGNMENT, font=FONT_STYLE_1)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALLIGNMENT, font=FONT_STYLE_1)
        self.goto(0, -20)
        self.write("(click on screen to exit)", align=ALLIGNMENT, font=FONT_STYLE_2)


