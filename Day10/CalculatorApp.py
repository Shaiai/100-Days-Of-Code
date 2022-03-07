#Caclulator application
import calc_art
#Function to handle addition.
def add(n1,n2):
    return n1 + n2

#Function for subtraction.
def subtract(n1,n2):
    return n1 - n2

#Function for multiplication.
def multiply(n1,n2):
    return n1 * n2

#Function for division.
def divide(n1,n2):
    return n1/n2

#Dictionary of operation that holds the functions we want to use in our calculator app later. If they choose '+' we use the add function on their inputs.
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

#
def calculator():
    #Prints the calculator logo when they decide to fresh start.
    print(calc_art.logo)
    #Boolean to handle the while loop, allowing for multiple calculations.
    calculating = True

    #Ask the user which number they would like to use for the calculation.
    num1 = float(input('What\'s the first number? '))

    while calculating:
        #Print out their operation options and ask them which they would like to perform.
        #i.e '+' = addition
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")

        #Ask user for the second number they'd like to apply the operation to.
        num2 = float(input('What\'s the second number? '))

        curr_num = operations[operation_symbol](num1,num2)
        #Print the results of numbers and chosen operation.
        print(f'{num1} {operation_symbol} {num2} is equal to: {round(operations[operation_symbol](num1,num2),2)}')

        #Ask the user if they'd like to continue calculating
        answer = input(f'Would you like to keep calculating with {curr_num}? Yes or No? or would you like to start a new by typing New? ').lower()

        #If they want to start a new, we recursively this function to get a fresh first input.
        if answer == 'new':
            calculator()
        #If the user chooses yes we then set a new num 1 to perform operations on and continue the while loop.
        if answer == 'yes':
            print(f'What operation would you like to perform on {curr_num}?')
            num1 = curr_num
            continue
        #If they choose no we break the while loop and end the program.
        if answer == 'no':
            print('Thank you for using our calculator today, goodbye!')
            calculating = False
            break

calculator()