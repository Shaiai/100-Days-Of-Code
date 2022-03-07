import caesar_art
#Reference alphabet for indexes we'll use later.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Global boolean to very whether or not they want to keep using the program later.
cipher = True

def caesar(text, shift, direction):
    message = []
    #If they choose decode over encode we will then shift the messages letters backwards to decode the mesage.
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            #Get the current index of the letter you're checking.
            x = alphabet.index(char)
            #Add to your blank string, the current letter shifted the proper amount of indexes to either encode or decode the message.
            message.append(alphabet[x + shift]) 
         #If the character is special or not in the alphabet we will simply append without any shifting.
        else:
            message.append(char)
    #Join our list of characters back together as as tring and output a verifying message showing the encoded or decoded message.
    return f"Your {direction}d message is {''.join(message)}"


print(caesar_art.logo) 
while cipher:
    #Get user input of wheter to encrypt, deisred message, and shifted index.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) %26 
    #Print their results.
    print(caesar(text, shift, direction))
    #Verify whether or not they'd like to continue using this program.
    answer = input('Would you like to encode or decode again? "Y" or "N"\n').lower()
    if answer == 'y':
        continue
    else:
        print('Thank you for playing with our cipher. G\'bye! ヽ(＾▽＾)人(＾▽＾)人(＾▽＾)ﾉ')
        cipher = False
