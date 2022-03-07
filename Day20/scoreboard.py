from turtle import Turtle
ALIGHNMENT = 'center'
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)   
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGHNMENT, font=FONT)
    
    def game_over(self):
        #self.clear()
        self.goto(0,0)
        self.write(f"Game Over.", False, align=ALIGHNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
