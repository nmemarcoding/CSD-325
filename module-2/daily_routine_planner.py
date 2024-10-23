# Name: Nima Memarzadeh 
# Date: 10/23/2024 
# Assignment: Module 2.2

"""
    This program is a daily routine planner.
"""

def get_yes_no_input(prompt):
    """Helper function to get a valid yes/no input from the user."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def make_smoothie():
    """Decides the ingredient for the smoothie."""
    banana_available = get_yes_no_input("Do you have a banana? (yes/no): ")
    if banana_available == 'yes':
        print("Using banana for smoothie.")
    else:
        print("Using oats for smoothie.")
    print("Drink smoothie.")

def setup_study_sessions():
    """Sets up the number of study sessions based on whether it's a workday."""
    is_workday = get_yes_no_input("Is it a workday? (yes/no): ")
    if is_workday == 'yes':
        return 4  # Set up 4 study sessions for a workday
    else:
        return 5  # Set up 5 study sessions for a non-workday

def study_routine(max_sessions):
    """Handles the study routine."""
    study_sessions = 0
    while study_sessions < max_sessions:
        print(f"Study session {study_sessions + 1}: Studying for 50 minutes.")
        print("Break for 10 minutes.")
        study_sessions += 1

    return study_sessions

def after_study_routine():
    """Decides what to do after completing study sessions."""
    finished_early = get_yes_no_input("Did you finish early? (yes/no): ")
    if finished_early == 'yes':
        print("Watch TV.")
      
    has_time_to_cook = get_yes_no_input("Do you have time to cook lunch? (yes/no): ")
    if has_time_to_cook == 'yes':
        ingredients_available = get_yes_no_input("Do you have the ingredients at home? (yes/no): ")
        if ingredients_available == 'yes':
            print("Cook food.")
        else:
            print("Order food online.")
    else:
        print("Order food online.")

def eat_lunch():
    """Handles the lunch step."""
    print("Eat lunch.")
    print("End of routine.")

def daily_routine():
    """Orchestrates the daily routine."""
    print("Wake up at 7 AM.")
    make_smoothie()
    print("Head to room and start studying.")
    max_sessions = setup_study_sessions()
    study_sessions_completed = study_routine(max_sessions)
    if study_sessions_completed >= max_sessions:
        after_study_routine()
    eat_lunch()

def main():
    """Main function to run the daily routine."""
    daily_routine()

# Run the main function
if __name__ == "__main__":
    main()
