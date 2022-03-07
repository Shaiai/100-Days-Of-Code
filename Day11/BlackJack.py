############### Blackjack Project #####################
import random
import BlackJackArt
import os
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### The making of the game #####################

#Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(lst):
    dealt = random.choice(cards)
    return dealt

#Create a function called calculate_score() that takes a List of cards as input.
#and returns the score. 
def calculate_score(lst):

    if sum(lst) == 21 and len(lst) == 2:
        return 0
    
    if 11 in lst and sum(lst) > 21:
        lst.remove(11)
        lst.append(1)
    
    return sum(lst)

#Function to compare the user and dealer's score and indicate who wins.
def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw, Sadge"
    elif computer_score == 0:
        return "The user has lost, the Dealer has a blacjack"
    elif user_score == 0:
        return "The player has won, he has a blackjack!"
    elif user_score > 21:
        return "The player busts! LOSS"
    elif computer_score > 21:
        return "The dealer has bust! YOU WIN"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

#Wrapper function to house our functions and game process for replayability.  
def play_game():
    #Print the game's title logo.
    print(BlackJackArt.logo)

    #Create the computer and player's hands.
    user_cards = []
    computer_cards = []
    is_game_over = False

    #Deal both the computer and the player 2 cards.
    for _ in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    #This while loop will handle the player's turn.
    while not is_game_over:
        #Check to see if the player or the computer have won the game. 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        #Show the player's hand and the dealer's first car in round 1.
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f'Computer\'s first card: {computer_cards[0]}')

        #Check to see if the user or computer got a blackjack and ask if the user would like another card.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_deal = input('Would you like to hit or hold: ').lower()
            if should_deal == 'hit':
                user_cards.append(deal_card(cards))
            else:
                is_game_over = True

    #This while loop will handle the dealer's turn.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards)) 
        computer_score = calculate_score(computer_cards)
    #Show the final results of the game before revealing the winner.
    print(f'Your final hand is: {user_cards}, your final score: {user_score}')
    print(f'Dealer\'s final hand: {computer_cards}, dealer\'s final score: {computer_score}')
    print(compare(user_score, computer_score))

#Ask the user if they'd like to play again. Clear the console and make a new instance of the game.
while input('Would you like to play a game of Blackjack? Yes or No?').lower() == 'yes':
    os.system('cls')
    play_game()

