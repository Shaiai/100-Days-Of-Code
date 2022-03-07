from msvcrt import ungetwch
import turtle
import pandas

#Set up the screen for our game.
screen = turtle.Screen()
screen.title('U.S. States Game')
image = "Day25\\us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Open the file and read it.
data = pandas.read_csv("Day25\\us-states-game-start\\50_states.csv")
all_states = data.state.to_list()
guessed_states = []

#Check if they've guessed all states
while len(guessed_states) < 50:
    #Take a guess from the user and have them guess another state.
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 correct", 
                                    prompt="What's another state's name?").title()
    #Check if the user wants to end the game.
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        #Turn the unguessed states into a table dataframe for export.
        new_data = pandas.DataFrame(missing_states, columns = ['Missed'])
        #Export the newly created table to the designated folder/directory.
        new_data.to_csv("Day25\\us-states-game-start\\To_Study.csv")

        break
    #check if the entered state is within our list of states and if so, write it on the correct state.
    if answer_state in all_states:
        guessed_states.append(answer_state)
        #Create our turtle to draw/write our state names.
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        #t.write(state_data.state.item())

