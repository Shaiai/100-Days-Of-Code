import coffee_art
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


#####GLOBALS#####
can_make = True
money = 0
ordering = True
################

def get_money():
    total = 0
    total += int(input('How many quarters?: ')) *25
    total += int(input('How many dimes?: ')) *10
    total += int(input('How many nickels?: ')) * 5
    total += int(input('How many pennies?: ')) * 1

    return total / 100

#Print the coffee shop welcome that is stored in a different py file we imported.    
print(coffee_art.logo)
#Loop to contain the functionality of the program.
while ordering == True:

    for resource in resources:
        print(f'{resource}: {resources[resource]}')

    #Ask the user what kind of drink they would like.
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    #If the user requests a report show them our current status of our resources.
    if drink == 'report':
        for ingredient in resources:
           print(f"{ingredient}: {resources[ingredient]}")
    
    if drink == 'off':
        print('Thank you for shopping with us today!')
        ordering == False
        break

    #Ask the user how much they are wanting to spend on this drink.
    to_spend = get_money()


    #If the user doesn't have enough money we prompt them and do not add to our total.
    if to_spend < MENU[drink]['cost']:
        print('That is not enough money, you are refunded.')
    
                #Check to see if we have the ingredients available to make their drink before we charge them.
    for ingredient in MENU[drink]['ingredients']:
         if MENU[drink]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry, we do not have enough {ingredient}. Your money has been refunded.")
            can_make = False
            break

    #If they have a suitable amount of money we do the suitable actions.
    if to_spend >= MENU[drink]['cost'] and can_make:
        #Tell the user their change and how much money they have in pocket now.
        print(f"Here is your change ${round((to_spend - MENU[drink]['cost']),2)}.")
        #Update the amount of money we have in our resources.
        resources['money'] += MENU[drink]['cost']
        #Tell the user they have ordered their drink successfully and tell them to enjoy.
        print(f'Here is your {drink} ☕ Enjoy!')
        #Update the amount of resources we have for the next drink.
        for ingredient in MENU[drink]['ingredients']:
            resources[ingredient] -= MENU[drink]['ingredients'][ingredient]
    
   
    







