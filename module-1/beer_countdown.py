# Name: Nima Memarzadeh
# Date: 10/22/2024
# Assignment: Module 1.3

"""
    This program is a simple beer bottle countdown application.
"""

def get_positive_integer(prompt):
    """
    Prompts the user to enter a positive integer.
    Repeats until a valid input is received.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: A validated positive integer input by the user.
    """
    while True:
        try:
            user_input = input(prompt)
            number = int(user_input)
            if number <= 0:
                print("Please enter a positive integer greater than zero.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def countdown_bottles(number):
    """
    Counts down the number of bottles from the given number to 1,
    displaying the lyrics for each number of bottles.

    Args:
        number (int): The starting number of bottles.
    """
    for i in range(number, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.\n")
        elif i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more beer!\n")


def main():
    """
    The main function that runs the beer bottle countdown application.
    """
    print("Welcome to the 'Bottles of Beer on the Wall' Countdown!")
    print()
    number_of_bottles = get_positive_integer("How many bottles of beer are on the wall? ")
    print("\nStarting the countdown...\n")
    countdown_bottles(number_of_bottles)
    print("Don't forget to buy more beer!\n")
    print("Thank you for using the Beer Bottle Countdown App. Cheers!")

if __name__ == "__main__":
    main()