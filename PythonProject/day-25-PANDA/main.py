# ----------------For Panda
import math

# Quick Check
# with open('./weather_data.csv ') as weather_file:
#     weather_list = weather_file.readlines()
#     print(weather_list)
# import  csv
#
#
# with open('./weather_data.csv') as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         temp_value = row[1]
#         if temp_value != 'temp':
#             temperatures.append(int(temp_value))
#     print(temperatures)

# import pandas
# from numpy.ma.extras import average
# # Getting data from Row
# weather_data = pandas.read_csv('weather_data.csv')
# # print(weather_data[weather_data.temp == weather_data.temp.max()])
# # max_day = weather_data.temp.max()
# # print(max_day)
#
#
# monday = weather_data[weather_data.day == 'Monday']
# fahrenheit= (monday.temp*1.8) + 32
# print(f'Fahrenheit :  {fahrenheit}')
import pandas

'''c_count = 0
b_count = 0
g_count = 0

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color = data['Primary Fur Color'].to_list()
for x in color:
    if x == 'Gray':
        g_count+=1
    elif x == 'Cinnamon':
        c_count+=1
    elif x == 'Black':
        b_count+=1
print(f'Black Count = {b_count}\nGray Count = {g_count}\nCinnamon Count = {c_count}')

data_dict = {
    'Fur Color': ['Black' , 'Gray', 'Cinnamon'],
    'Fur Count':[b_count,g_count,c_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv('squirrelCount.csv')'''

data = pandas.read_csv('weather_data.csv')
days = data['day']
monday = data[data.day == 'Monday']
print(monday.day)
data_dict = {
    'students' : ['Amy', 'Edward', 'Timothy'],
    'grades':[89,78,79]
}
df = pandas.DataFrame(data_dict)
df.to_csv('new_data.csv')

