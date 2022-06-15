from turtle import Turtle





class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('gray')
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.score = 0
        with open('highscore.txt') as file:
            file = int(file.read())
        self.high_score = file

    def write_score(self):
        self.clear()
        self.goto(0, 260)
        self.pendown()
        self.write(f"Score: {self.score} and High Score: {self.high_score}", False, align="center", font=('Arial', 15,
                                                                                                          'normal'))

    def new_point(self):
        self.score += 1

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER", False, align="center", font=('Arial', 20, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0


