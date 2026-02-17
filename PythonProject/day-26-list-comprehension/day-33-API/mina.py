import requests
import datetime as dt
import smtplib
import time
MY_EMAIL = 'arleeilives@gmail.com'
PASSWORD= 'umcrjmayrjvwgkot'

MY_LAT = 27.999020  #Your Latitude
MY_LNG = -80.672661  #Your Longitude


def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    longitude = float(response.json()['iss_position']['longitude'])
    latitude = float(response.json()['iss_position']['latitude'])


    if MY_LAT-5 <= latitude <= MY_LAT and MY_LNG-5 <= longitude <= MY_LNG+5:
            return True
    else:
        False

def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    date = dt.datetime.now().hour
    if date >=sunset or date<=sunrise:
        return True
    else:
        False
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs='nkrumahhpearson@gmial.com', msg='Subject: Look Up\n\nHeyy, THe ISS is in  the sky:)')
