# Name: Nima Memarzadeh
# Date: 05/12/2024
# Assignment: Module 9.2
import requests
import json

def test_api_connection(url):
    """Test the API connection."""
    try:
        response = requests.get(url)
        print(f"API Connection Test: Status Code {response.status_code}")
        if response.status_code == 200:
            print("Connection successful!")
        else:
            print("Failed to connect.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_starship_data(starship_id):
    """Fetch data about a starship from the API."""
    try:
        url = f"https://swapi.dev/api/starships/{starship_id}/"
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad responses
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

def display_unformatted_response(response):
    """Display the raw response from the API."""
    print("\nUnformatted Response:")
    print(response.text)

def display_formatted_response(response):
    """Display the formatted JSON response."""
    starship_data = response.json()
    print("\nFormatted Response:")
    print(json.dumps(starship_data, indent=4))

    # Additional details for better readability
    print("\nAdditional Details: for better readability")
    print("\nStarship Details:")
    print(f"Name: {starship_data.get('name', 'N/A')}")
    print(f"Model: {starship_data.get('model', 'N/A')}")
    print(f"Manufacturer: {starship_data.get('manufacturer', 'N/A')}")
    print(f"Cost in Credits: {starship_data.get('cost_in_credits', 'N/A')}")
    print(f"Length: {starship_data.get('length', 'N/A')} meters")
    print(f"Crew: {starship_data.get('crew', 'N/A')}")
    print(f"Passengers: {starship_data.get('passengers', 'N/A')}")

def main():
    """Main function to run the program."""
    # Base URL for Starship data
    base_url = "https://swapi.dev/api/starships"

    # Starship ID to fetch data for (Millennium Falcon as an example)
    starship_id = 10

    # Step 1: Test the API connection
    test_api_connection(base_url)

    # Step 2: Fetch starship data
    response = fetch_starship_data(starship_id)
    if response:
        # Step 3: Print unformatted response
        display_unformatted_response(response)

        # Step 4: Print formatted response
        display_formatted_response(response)

if __name__ == "__main__":
    main()
