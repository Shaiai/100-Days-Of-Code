student_dict = {
    "student": ['Angela','James','Lily'],
    "score": [56,76,98]
}

#Looping through dictionaries:
#for(key, value) in student_dict:
#    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

#Loop through a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)