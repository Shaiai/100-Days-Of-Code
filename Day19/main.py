from operator import is_
from turtle import Turtle, Screen
import turtle
import random

#Screen set up
screen = Screen()
screen.setup(width=500,height=400)
#Ask the user to make a bet.
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
#Turtle attributes for use later
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80 ]
is_race_on = False
all_turtles = []

#Create six turtle for the race all with different colors from the rainbow.
for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

#Check if the user made the bet.  
if user_bet:
    is_race_on = True

#While there is a bet and the race is still going -> Do things
while is_race_on:
    #Loop through all the turtles.
    for turtle in all_turtles:
        #If they are at the end of the screen.
        if turtle.xcor() > 230:
            is_race_on = False
            #Get the color of the winning turtle for the congratulations or loss message.
            winning_color = turtle.pencolor()
            #If the user's bet was correct or wrong do either.
            if winning_color == user_bet:
               print(f"You've won the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle was the winner!")
        
        #Make a random number and move the current turtle forward that much.
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        
#Exit the game when the user clicks after all functionality.
screen.exitonclick()