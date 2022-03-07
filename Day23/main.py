import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Setting up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#Initializing a player.
player = Player()

#Initialize the car manager.
car_manager = CarManager()

#Initialize a scoreboard.
scoreboard = Scoreboard()

#Move the player forward when the up key is pressed.
screen.onkey(player.player_up, "Up")

game_is_on = True
while game_is_on:

    #Refresh the screen every 0.1 seconds. This is to imitate a framerate.
    time.sleep(0.1)
    screen.update()

    #Generate cars and make them move with methods in class.
    car_manager.create_car()
    car_manager.move_cars()

    #Check for Collision between player and cars.
    if player.got_hit(car_manager):
        scoreboard.game_over()
        game_is_on = False

    #See if the player won.
    if player.player_level_up(car_manager):
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.level_increase()
        

screen.exitonclick()