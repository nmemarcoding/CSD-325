# Name: Nima Memarzadeh
# Date: 05/12/2024
# Assignment: Module 9.2
import requests

# Test connection to Google's website
response = requests.get('http://www.google.com')
print(response.status_code)
