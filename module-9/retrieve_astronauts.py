# Name: Nima Memarzadeh
# Date: 05/12/2024
# Assignment: Module 9.2
import requests
from datetime import datetime, timezone

def get_iss_location():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    position = data['iss_position']
    latitude = position['latitude']
    longitude = position['longitude']
    timestamp = datetime.fromtimestamp(data['timestamp'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    print(f"As of {timestamp} UTC, the ISS is at latitude {latitude} and longitude {longitude}.")

def get_astronauts():
    url = 'http://api.open-notify.org/astros.json'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    print("\nAstronauts in space:")
    print("=====================================")
    print(data)

    print("\nBetter formatted results:")
    print("-------------------------------------")
    print(f"\nThere are {data['number']} astronauts in space right now:\n")
    for person in data['people']:
        print(f"{person['name']} aboard the {person['craft']}")

def main():
    try:
        get_iss_location()
        get_astronauts()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
