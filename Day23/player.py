from turtle import Turtle
from car_manager import CarManager
#Global variables to help set up
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.go_to_start()
        self.setheading(90)
   
   #Method to move player forward.
    def player_up(self):
        self.forward(MOVE_DISTANCE)
    
    #Method to detect collision between player and cars.
    def got_hit(self, car_manager):
        for car in car_manager.all_cars:
            if self.distance(car) < 20:
                print('Player got Hit')
                return True
    
    #Return the turtle to the start of the game again. This is for game_over or Level_up
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    #Method to check if the player has reached the finish line.
    def player_level_up(self, car_manager):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    
