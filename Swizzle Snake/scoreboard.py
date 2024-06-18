from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.draw_line()
        self.hideturtle()
        self.pu()
        self.color('white')
        self.setpos(0, 260)
        self.score = 0
        self.update_scoreboard()

    #Increases the player's score.
    def up_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    #Updates the scoreboard.
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    #Draws the upper boundary line.
    def draw_line(self):
        ld = Turtle()
        ld.hideturtle()
        ld.setpos(-300, 250)
        ld.color('white')
        ld.width(2)
        ld.pd()
        ld.forward(600)

    #Prints "GAME OVER" when the player loses.
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)