from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 27, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_display()
        self.update_scoreboard()

    def score_display(self):
        """
        Shows score on HUD.
        """
        self.hideturtle()
        self.penup()
        self.goto(0, 262)
        self.color('white')

    def update_scoreboard(self):
        """
        Updates score display with current score.
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        End game.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        """
        Increment score by 1.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()






