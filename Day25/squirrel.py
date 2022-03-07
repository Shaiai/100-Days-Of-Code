import pandas

#Open and read the squirrel data csv
data = pandas.read_csv('Day25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

#Return the fur data as a list.
fur_list = data["Primary Fur Color"].to_list()

#Create a dictionary to hold data and later format our table.
squirrel_dict = {
    "Fur Color": ['Gray', 'Red', 'Black'],
    "Count": []
}

#Add the different colros of fur and their respective counts to the dictionary.
squirrel_dict["Count"].append(fur_list.count('Gray'))
squirrel_dict["Count"].append(fur_list.count('Black'))
squirrel_dict["Count"].append(fur_list.count('Cinnamon'))

#Turn our dictionary into a neatly organized data frame. 
squirrel_data = pandas.DataFrame(squirrel_dict)

#Export our new dataframe with our data into a csv file.
#squirrel_data.to_csv("Day25\\squirrel_count.csv")