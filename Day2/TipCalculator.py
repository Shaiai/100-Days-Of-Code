
bill = float(input("What was the total of your bill? $"))
percentage = int(input("What percent tip would you like to leave: 10,12 or 15%?"))
num_people = int(input("How many people have to split the bill?"))

final_bill = round(bill + (bill * (percentage/100)),2)
your_pay = final_bill / num_people

print(f'Your final bill is {"{:.2f}".format(final_bill)} with tip. Split among {num_people} you have to pay {your_pay}')

