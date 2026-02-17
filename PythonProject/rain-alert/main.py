import requests

api_key= '26fec6a0daa501b0efe8934469002998'
parameters = {
    'lat':28.034462,
    'long':-80.588661,
    'appid':api_key,
    'cnt': 4
}
response = requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=28.034462&lon=-80.588661&appid=26fec6a0daa501b0efe8934469002998',params=parameters)
response.raise_for_status()
weather_data = response.json()
print(response)
#
# weather_ids = [ x['weather'][0]['id'] for x in weather_data['list']]
# for x in weather_ids:
#     if x < 700:
#         print('Bring an Umbrella')

print(weather_data)

