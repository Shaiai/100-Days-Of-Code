from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.write(f"Level: {self.level}", align ='left', font=FONT)
    
    #Clear old score information and update upon stage win.
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align ='left', font=FONT)

    #This will increase the level text when the turtle wins a stage.
    def level_increase(self):
        self.level += 1
        self.update_scoreboard()
    
        
    #Method that creates the gameover screen when the turtle is hit.
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER! Sadge", align ='center', font=FONT)