
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    #This will create a car at a random y-coordinate and give them a random color from our list of colors.
    def create_car(self):
        random_choice = random.randint(1,8)
        if random_choice == 1:
            new_car = Turtle('square')
            new_car.shape('square')
            new_car.penup()
            new_car.shapesize(stretch_wid= 1, stretch_len= 2)
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250,250)
            new_car.goto(300,y_position)
            new_car.setheading(180)
            self.all_cars.append(new_car)
        
    #This method moves the cars forward by the determined incremental speed.
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    #This method increases ths cars speed once the turtle reaches the next level.
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
