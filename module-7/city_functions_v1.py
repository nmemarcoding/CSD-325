# Name: Nima Memarzadeh
# Date: 11/28/2024
# Assignment: Module 7.2

def city_country(city, country):
    """Return a formatted string of city and country."""
    return f"{city.title()}, {country.title()}"

# Call the function at least three times
print("Initial Function Calls:")
print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
print(city_country('paris', 'france'))
