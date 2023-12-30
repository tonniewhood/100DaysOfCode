import requests
import smtplib
import time
from datetime import datetime


def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_time = (data["results"]["sunrise"].split("T")[1].split(":")[:2])
    sunset_time = (data["results"]["sunset"].split("T")[1].split(":")[:2])

    time_now = datetime.utcnow().time()

    if int(sunset_time[0]) <= time_now.hour <= int(sunrise_time[0]):
        if int(sunset_time[1]) < time_now.minute < int(sunrise_time[1]):
            return True
        else:
            return False
    else:
        return False


def iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5:
        if iss_longitude - 5 <= MY_LONG <= iss_longitude + 5:
            return True
        else:
            return False
    else:
        return False


MY_LAT = 41.058071 # Your latitude
MY_LONG = -111.985220 # Your longitude

while True:

    if iss_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="test4python15@gmail.com", password="latp nfuk dhry teqc")
            connection.sendmail(from_addr="test4python15@gmail.com",
                                to_addrs="woodanthony15@gmail.com",
                                msg="Subject:ISS\n\nLook up")

    time.sleep(60)
