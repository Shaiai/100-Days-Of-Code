import hangman_art
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
hang_stages = 6
guessed_letters = []
display = ['_'] * len(chosen_word)
guessed = False

#Testing code
print(hangman_art.logo,'\n')


while not guessed:
    print(chosen_word)
    guess = input("Guess a letter: ").lower()
    player_guess = ''

    for x in range(len(chosen_word)):
        if chosen_word[x].lower() == guess:
            display[x] = chosen_word[x]
    if guess not in chosen_word:
        hang_stages -= 1
        print(f'These are the letters you\'ve guessed\n {guessed_letters}')
        print(hangman_art.stages[hang_stages])
    if hang_stages == 0:
        print(f'You are out of guesses LOSER, the word was {chosen_word}')
        break
    print(display)

    if guess in guessed_letters:
        print("You've already guessed this one IDIOT!")
    guessed_letters.append(guess)
    
    wanna_guess = input('Would you like to guess the word? Yes or No?').lower()

    if wanna_guess == 'yes':
        player_guess = input('Please take your guess: ')

    if player_guess == chosen_word:
        print(f'You have guessed the word! It WAS {chosen_word}')
        guessed = True
        break

    if player_guess != chosen_word:
        hang_stages -= 1
        print(f'These are the letters you\'ve guessed\n {guessed_letters}')
        print(hangman_art.stages[hang_stages])
        print('You have the guessed the wrong word, moron')

    if ''.join(display) == chosen_word:
        print(f'You have guessed the word! It WAS {chosen_word}')
        guessed = True
        break




