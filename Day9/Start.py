programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

#print(programming_dictionary['Loop'])

'''
programming_dictionary["Tomatoe"] = "Something you throw at a struggling artist when they're trying their best."

programming_dictionary["Bug"] = "A moth inside of your computer"

for keys in programming_dictionary:
    print(f'{keys}: {programming_dictionary[keys]}')


#Nesting

travel_log = {
    "France": ['Paris','Lille','Dijon'],
    "Germany": ['Berlin','Hamburg','Stuttgart']
}
'''

#Nesting a dictionary in a dictionary
'''
travel_log = {

    "France": {"cities_visited": ['Paris','Lille','Dijon'], 'total_visits': 12},
    "Germany": ['Berlin','Hamburg','Stuttgart']
}
'''
#Dictionaries nested in a list
travel_log = [ 
    {
    'country': 'France',
    'cities_visited': ['Paris','Lille','Dijon'],
    'total_visits': 12
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin','Hamburg','Stuttgart'],
        'total_visits': 5
    }
]


