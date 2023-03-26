from dotenv import load_dotenv
import requests
import os
from datetime import datetime
from requests.auth import HTTPBasicAuth
load_dotenv()

url = "https://trackapi.nutritionix.com"
APPLICATION_ID = os.getenv("APPLICATION_ID")
APPLICATION_API = os.getenv("APPLICATION_API")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOKEN = os.getenv("TOKEN")
ENDPOINT_SHEETY = os.getenv("ENDPOINT_SHEETY")

authintication = HTTPBasicAuth(USERNAME, PASSWORD)

print(USERNAME, PASSWORD)
query_input_text = input("Tell me which exercises you did: ")

headers ={
    "Content-Type": "application/json",
    "X-APP-ID": APPLICATION_ID,
    "X-APP-KEY": APPLICATION_API,
}

parameters ={
    # "query":"Ran 2 miles and walked for 3 KM.",
    "query":query_input_text,
    "gender":"male",
    "weight_kg":70,
    "height_cm":163.64,
    "age":23
}

endpoint = f"{url}/v2/natural/exercise"

response = requests.post(url=endpoint, json=parameters, headers=headers)
result = response.json()

print(response)
# print(result)

today = datetime.now()

date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

outputs = []
for output in result['exercises']:
    new_record = {
        "date": date,
        "time": time,
        "exercise": output["name"].title(),
        "duration": output["duration_min"],
        "calories": output["nf_calories"],
    }
    outputs.append(new_record)

    parameters_sheety = {
            "workout": new_record
    }
    response_sheety = requests.post(url=ENDPOINT_SHEETY,
                                    json=parameters_sheety,
                                    auth=authintication
                                )
    result_sheety = response_sheety.json()
    print(result_sheety)
    print(response_sheety)
    
    
print(outputs)
