print("Welcome to the rollercoaster")
height = int(input('Please enter your height:'))

if height > 120:
    print("Congrats you're tall enough for the ride")
    age = int(input("Please tell me your age: "))
    if age < 12:
        print("You'll have to pay $5")
    elif age <= 18:
        print("You'll have to pay $7")
    else:
        print("Adults have to pay $12")

else:
    print("Please find a new ride this one is for big boys")