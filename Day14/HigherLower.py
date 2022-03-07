import random
import game_data
import HL_art
import os


#Wrapper function to hold the games looping and fucntionality.
def high_or_low():
    #Score holder
    score = 0
    #Boolean to keep the loop running until the player guesses wrong.
    guessed_wrong = False
    while not guessed_wrong:
        #Pull a random character a and random character b from the data dictionary.
        compare_a = random.choice(game_data.data)
        compare_b = random.choice(game_data.data)
        #print the higher/lower logo at the start of our game.
        print(HL_art.logo)
        ###########print the values to be able to check game's functionality#########
        #print(compare_a['follower_count'])
        #print(compare_b['follower_count'])
        ###########                                                         #########
        #print the random character A and their information, excluding their follower count.
        print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
        print(HL_art.vs)
        #print the random character B and their information, excluding their follower count.
        print(f"Against: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}")
        #Ask the user to guess who has more followers.
        guess = input('Who has more followers? Type "A" or "B"').lower()
        #Check the followers of a and b and compare them. Then respond accordingly.
        if guess == 'a' and compare_a['follower_count'] > compare_b['follower_count']:
            score += 1
            print(f'That was the correct guess! Current score: {score}')
        elif guess == 'b' and compare_a['follower_count'] < compare_b['follower_count']:
            score += 1
            print(f'That was the correct guess! Current score: {score}')
        else:
            #Clear the system and print out the logo as well as the final score for the user.
            os.system('cls')
            print(HL_art.logo)
            print(f'Sorry bucko, that was the wrong answer. Final Score: {score}')
            guessed_wrong = True
            break
    #Ask if they'd like to play again and recursively call the function again.
    while input('Would you like to play again? "Yes" or "No"').lower() == 'yes':
        high_or_low()

high_or_low()
        
    
