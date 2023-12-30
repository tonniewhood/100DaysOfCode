
import requests
from datetime import datetime

NUTRITIONIX_APP_ID = "bf5beeec"
NUTRITIONIX_API_KEY = "19de20033bc085da41c8c0d0425e9a01"
NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

nutritionix_parameters = {
    "query": "I did 15 pullups",
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 190,
    "age": 22
}

response_raw = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT, headers=nutritionix_headers, data=nutritionix_parameters)

today = datetime.now()

date = today.strftime("%m/%d/%Y")
time = today.strftime("%H:%M:%S")

response = response_raw.json()["exercises"][0]
exercise = response["name"]
duration = response["duration_min"]
calories = response["nf_calories"]

# print(f"{'Date':12s}|{'Time':12s}|{'Exercise':20s}|{'Duration':15s}|{'Calories':5s}")
# print(f"{date:12s}|{time:12s}|{exercise:20s}|{duration:<15d}|{calories:<5d}")

SHEETY_ENDPOINT = "https://api.sheety.co/cfda42ddc48a36a5363894b4f599c821/myWorkoutsTony/workouts"
SHEETY_AUTH_TOKEN = "Ry73utOtmPWA7t9ksp6seYcvCexhXmiD"

sheety_header = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}",
    "Content-Type": "application/json",
}

body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_header, json=body)

print(sheety_response.text)
