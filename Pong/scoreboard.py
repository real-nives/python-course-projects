from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 300)
        self.write(self.p1_score, align='center' , font=('Courier', 80, 'normal'))
        self.goto(150, 300)
        self.write(self.p2_score, align='center' , font=('Courier', 80, 'normal'))

    def p1_point(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2_point(self):
        self.p2_score += 1
        self.update_scoreboard()

    def winner(self, big_winner):
        self.clear()
        self.goto(0, 0)
        self.write(f"{big_winner} Won!", align='center' , font=('Courier', 40, 'normal'))