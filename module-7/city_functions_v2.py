# Name: Nima Memarzadeh
# Date: 11/28/2024
# Assignment: Module 7.2

def city_country(city, country, population=None):
    """Return a formatted string of city and country with optional population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"

# Call the function with different parameter combinations
print("Population Optional Function Calls:")
print(city_country('santiago', 'chile'))
print(city_country('santiago', 'chile', 5000000))
print(city_country('tokyo', 'japan', 13929286))
print(city_country('paris', 'france', 2140526))
