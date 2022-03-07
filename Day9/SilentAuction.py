import silent_art
import os

bidding = True
taken_bids = {
}

#Function to add a key and value to the dictionary.
def take_bid(name,bid):
    taken_bids[name] = bid

#Definition that loops through the keys and values to determine the winner.
def check_winner(dictionary):
    winner = ''
    winning_bid = 0
    for key in dictionary:
        if dictionary[key] > winning_bid:
           winner = key
           winning_bid = dictionary[key]   
    print(f'The winner of the acution is {winner}\nWith a bid of: {winning_bid}')   
    pass

#While there are still more bidders we run this loop.
while bidding:

    #Prints logo from art file.
    print(silent_art.logo)
    
    #Ask for name(Key) and bid(value) and adding them to the dictionary.
    name = input('Please input your name: ')
    bid = int(input('How much would you like to bid? $'))
    take_bid(name, bid)
    #Check to see if there are more bidders and if we are continuing the loop.
    bid_status = input('Are there any more bidders? Yes or No? ').lower()

    #If still bidding we clear the console for the next blind acutioner and continue the loop.
    if bid_status == 'yes':
        os.system('cls')
        continue
    #If there are no more auctioniers we check for the winner, print the results and break from the loop.
    else:
        #print(taken_bids)
        #print(taken_bids[name])
        check_winner(taken_bids)
        bidding = False
        break