import random
import number_art
import os

#Number Guessing Game Objectives:
to_guess = random.randint(0,100)
# Track the number of turns remaining.
num_turns = 0

#Function that will compare the goal and the players guess then return the corresponding variable.
def check_answer(goal,guess):
    if guess > goal:
        return 'h'
    if guess < goal:
        return 'l'
    if guess == goal:
        return 'e'

#Wrapper function to host our game amake recursive gameplay possible.
def guess_again():
    #Boolean to keep the game rolling until the number is guessed correctly.
    is_guessed = False
    # Include an ASCII art logo.
    print(number_art.logo)
    print("I'm thinking of a number between 1 and 100.")

    # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
    difficulty = input('Please choose a difficulty. Type "Easy" or "Hard"').lower()
    if difficulty == 'easy':
        num_turns = 10
    else:
        num_turns = 5
    print(f'Okay player, you get {num_turns} guesses. Good Luck!')
    
    #While the player hasn't guessed the number yet, we keep playing.
    while not is_guessed:
        # Allow the player to submit a guess for a number between 1 and 100.
        player_guess = int(input('Guess a number between 1 and 100 player!: '))

        #Compare the user's guess to the number to be guessed and respond to them accordingly.
        got_it = check_answer(to_guess, player_guess)
        if got_it == 'h':
            print('Oops user, you\'ve guessed too high!')
        if got_it == 'l':
            print('Haha baka user, you guessed too low!')
        if got_it == 'e':
            print(f'Wow user! that is incredible! the number WAS {to_guess}\n')
            is_guessed = True
            break
        
        #If the guess is incorrect we will either lower the amount of turns and warn them
        #Or we will tell them that they have run out of turns and lost.
        num_turns -= 1
        print(f'Be aware user, you only have {num_turns} turns left! D:\n')
        if num_turns == 0:
            print('Geez user you\'re not very good at this, you\'ve run out of turns\nBetter luck next time.')
            break
    
    #This is to ask the player if they'd like to start again with a clean slate.
    while input('Would you like to play again? type Yes or No').lower() == 'yes':
        #Clear the console and variables.
        os.system('cls')
        #Recursively call the function to being the loop a new.
        guess_again()
        
guess_again()





