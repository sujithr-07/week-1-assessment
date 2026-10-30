import csv
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

try:
    with open("employees.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        employees = list(reader)

    print(f"rows read: {len(employees)}", end="")

except FileNotFoundError:
    print("Error: employees.csv file not found.")
    raise SystemExit(1)

#write employees to json file
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print(" | ",end="")

#write high earners to high_earners.json file
high_earners = [
    employee 
    for employee in employees 
    if float(employee["salary"]) > 50000
]

with open("high_earners.json", "w") as file:
   fieldnames= employees[0].keys()
   writer = csv.DictWriter(file, fieldnames=fieldnames)
   writer.writeheader()
   writer.writerows(high_earners)

print(f"High earners: {len(high_earners)}")

#GET request to API
url= "https://jsonplaceholder.typicode.com/users"

headers = {}

if API_KEY:
    headers["X-API-Key"] = f"Bearer {API_KEY}"

try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()
    users = response.json()

    for user in users[:3]:  # Print only the first 3 users
        print(
            f"{user.get('id')} - " 
            f"{user.get('name')} - " 
            f"{user.get('email')}"
        )

#parse nested json using get method
    parsed_users = []

    for user in users:
        address = user.get("address", {})
        geo = address.get("geo", {})
        company = user.get("company", {})

        parsed_users.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": address.get("city"),
            "lat": geo.get("lat"),
            "lng": geo.get("lng"),
            "company_name": company.get("name")
        })

        with open("parsed_users.json", "w") as file:
            json.dump(parsed_users, file, indent=4)

except requests.exceptions.Timeout:
    print("Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Connection error occurred.")

except requests.exceptions.HTTPError as error:
    print(f"HTTP error: {error}")


#handle 404 response
try:
    response = requests.get("https://jsonplaceholder.typicode.com/invalid_endpoint", headers=headers, timeout=5)
    if response.status_code == 404:
        print("/users/9999 -> 404 Not Found")
    else:
        response.raise_for_status()
        print(response.json())

except requests.exceptions.Timeout:
    print("Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Connection error occurred.")

except requests.exceptions.HTTPError as error:
    print(f"HTTP error: {error}")