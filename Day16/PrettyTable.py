from prettytable import PrettyTable

#Create our table object
table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Squirtle','Charmander']) 
table.add_column('Type', ['Electric','Water','Fire'])
table.align = 'l'
table.border = True

print(table)