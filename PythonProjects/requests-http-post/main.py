import requests
from datetime import datetime

from requests import delete

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'arleeil'
TOKEN = 'kiakaiaksiosi'
user_params ={
    'token':'kiakaiaksiosi',
    'username':'arleeil',
    'agreeTermsOfService': 'yes',
    'notMinor' :'yes'

}
header = {
   'X-USER-TOKEN':TOKEN }


# Creating User Account - Post
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Making Graph
# graph_config={
#     'id':'graph1',
#     'name': 'my_habit_graph',
#     'unit': 'hours',
#     'type': 'int',
#     'color': 'sora',
#
# }
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
# response = requests.post(url=graph_endpoint,json= graph_config,headers = header )

# Placing Pixel
# today = datetime(year=2025, month=10,day=21)
# pixel_config ={
#     'date':today.strftime('%Y%m%d'),
#     'quantity': '6',
# }
# response = requests.post(url=f'{pixela_endpoint}/{USERNAME}/graphs/graph1', json=pixel_config, headers=header )

delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'
# Deleting Pixel
response = requests.delete(url=delete_endpoint ,headers = header)
print(response.text)


