#Import our modules from our other file's class definitions.
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import coffee_art

#Create instances of our objects from imported classes/modules 
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#Global varaibles not covered by attributes.
is_on = True

##################################################################### Begin Constructing Code##########################################################
print(coffee_art.logo)
while is_on:

    #Ask the user what they would like to drink.
    drink_choice = input(f'What yould you like? ({menu.get_items()}): ')
    #if the user types off we turn the machine off.
    if drink_choice == 'off':
        is_on = False
        break
    elif drink_choice == 'report':
        #Report to the employee what is available to them.
        coffee_maker.report()
        money_machine.report()
    #Check if we have suitable resources for that drink.
    if coffee_maker.is_resource_sufficient(menu.find_drink(drink_choice)):
        #Ask the user to insert coins and check if it is enough for the drink.
        if money_machine.make_payment(menu.find_drink(drink_choice).cost):
            #If they paid  enough and we have enough resources you can make the coffee.
            coffee_maker.make_coffee(menu.find_drink(drink_choice))



    