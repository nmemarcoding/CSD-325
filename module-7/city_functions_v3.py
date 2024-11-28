# Name: Nima Memarzadeh
# Date: 11/28/2024
# Assignment: Module 7.2

def city_country(city, country, population=None, language=None):
    """Return a formatted string of city and country with optional population and language."""
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, {language}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"

# Final function call demonstration
print("Final Function Calls Demonstration:")
print("No optional parameters:", city_country('santiago', 'chile'))
print("With population:", city_country('santiago', 'chile', 5000000))
print("With population and language:", city_country('santiago', 'chile', 5000000, 'Spanish'))
print("With different cities:")
print(city_country('tokyo', 'japan', 13929286, 'Japanese'))
print(city_country('paris', 'france', 2140526, 'French'))
