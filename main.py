from dotenv import load_dotenv
import requests
import os
load_dotenv()

url = "https://trackapi.nutritionix.com"
APPLICATION_ID = os.getenv("APPLICATION_ID")
APPLICATION_API = os.getenv("APPLICATION_API")

headers ={
    "Content-Type": "application/json",
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_API,
    'x-remote-user-id': '0',

}

parameters ={
    "query":"ran 3 miles",
    "gender":"male",
    "weight_kg":70,
    "height_cm":163.64,
    "age":23
}

endpoint = f"{url}/v2/natural/exercise"

response = requests.post(url=endpoint, params=parameters, headers=headers)
result = response.json()

print(result)