# Name: Nima Memarzadeh
# Date: 11/06/2024
# Assignment: Module 4.2

""" This program reads a CSV file containing 
    weather data for Sitka, Alaska, and allows 
    the user to view high and low temperatures 
    for each day in 2018. The user can choose to 
    view high temperatures, low temperatures, or exit the program. 
"""


import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys  # New import to handle exit

# Instructions for the user
def display_instructions():
    print("Welcome to the Weather Data Viewer!")
    print("Options:")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")
    print("Please enter the number corresponding to your choice.")

# Function to read the CSV file and extract data
def read_weather_data(filename):
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high, and low temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])  # Assuming the low temp is in column 6
            highs.append(high)
            lows.append(low)

    return dates, highs, lows

# Function to plot temperatures
def plot_temperatures(dates, temps, title, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    
    # Format plot
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Main function to control the menu and user selection
def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_weather_data(filename)

    while True:
        display_instructions()
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            print("Displaying high temperatures.")
            plot_temperatures(dates, highs, "Daily High Temperatures - 2018", "red")
        elif choice == '2':
            print("Displaying low temperatures.")
            plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", "blue")
        elif choice == '3':
            print("Thank you for using the Weather Data Viewer. Goodbye!")
            sys.exit()  # Exit the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main function
if __name__ == "__main__":
    main()
