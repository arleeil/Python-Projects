#

import pandas
# from numpy.ma.extras import average
#
# data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# max_weather = data['temp'].max()
# data_list = data[data.temp == max_weather]
# print(data_list)
#
# data2 = {'this is my dictionary'}
#
# data2_transformation = pandas.DataFrame(data2)
# data2_transformation.to_csv('new_data.csv')

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey = len(data[data['Primary Fur Color'] == 'Gray'])
cin = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {

    'Fur Color':['Grey', 'Cinnamon', 'Black'],
    'Fur Count': [grey , cin, black],
}

dt = pandas.DataFrame(data_dict)

dt.to_csv('squirrel_count.csv')






