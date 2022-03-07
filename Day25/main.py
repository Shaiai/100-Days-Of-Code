import csv
from re import S
import pandas 


'''
with open("Day25\\weather_data.csv") as data_file:
   data = data_file.readlines()
   print(data)   
'''
'''
with open("Day25\\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))  
    print(temperatures)
'''

#Have pandas neatly read and organize our data file.
#data = pandas.read_csv("Day25\\weather_data.csv")

'''#Turn our data file into a dictionary
data_dict = data.to_dict()

#This just creates a list of data fromn a column labeled 'temp' in our csv.
temp_list = data['temp'].to_list()

print(data['temp'])
#This is how to access the column temp using the dot method and finding the mean.
print(f"Your average temperatures is: {round(data.temp.mean(),2)}")
#This is how to access the column 'temp' using the string method and finding the max.
print(f"Your max temperature is: {data['temp'].max()}")
'''

#Get the conditions.
#print(data.condition)



#Get Data in rows of data frame.
#Print the row where the day is equal to 'Monday'
#print(data[data.day == 'Monday'])

#Find which row of data had the highest temperature in the week.
'''max_temp = data.temp.max()
print(data[data.temp == max_temp])
'''
#print(data[data.temp == data.temp.max()])

'''
monday = data[data.day == 'Monday']

print(int((monday.temp * 9/5) + 32))
'''

#Create a data_frame from scratch:
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
#Writing our new data to a csv file.
data = pandas.DataFrame(data_dict)
#data.to_csv("Day25\\new_data.csv")

print(data[data.scores == 65])