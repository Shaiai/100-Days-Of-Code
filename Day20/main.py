from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True

#Initialization of objects
snake = Snake()
food = Food()
score = Scoreboard()

#Listens for our keypress to call our snake functions for movement.
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:

    #This handles the screen updating to portray our movement.
    screen.update()
    #This is a timer that allows everything on the screen to do its proper movement in 0.1  seconds before giving feedback.
    time.sleep(0.1)
    
    snake.move()

    #Detect collision with the food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False
    
    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False


screen.exitonclick()