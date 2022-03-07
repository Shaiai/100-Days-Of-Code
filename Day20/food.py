from turtle import Turtle
import random

#Initialize the food class and pass the turtle class for inheretence.
class Food(Turtle):

    def __init__(self):
        #The super function call will initialize the food with all attributes of turtle. 
        super().__init__()
        #General set up for food pellet shape, size, color, animation speed.
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
        
    
    def refresh(self):
        #Get random coordinates within our screen's width and height.
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)