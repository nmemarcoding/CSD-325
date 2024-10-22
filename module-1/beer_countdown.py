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

