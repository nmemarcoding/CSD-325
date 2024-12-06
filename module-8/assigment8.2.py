# Name: Nima Memarzadeh
# Date: 05/12/2024
# Assignment: Module 8.2

import json

def print_student_list(student_list):
    """
    Print out student details in a formatted manner.
    """
    for student in student_list:
        print(f"{student['F_Name']} , {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

def main():
    try:
        # Load the original student list from JSON file
        print("Loading student.json file...")
        with open('student.json', 'r') as file:
            students = json.load(file)
        
        # Output original student list
        print("\n--- Original Student List ---")
        print_student_list(students)
        
        # Add new student with Nima's details
        new_student = {
            "F_Name": "Nima",
            "L_Name": "Memarzadeh",
            "Student_ID": 12345,
            "Email": "nmemarzadeh@example.com"
        }
        
        # Append new student to the list
        students.append(new_student)
        
        # Output updated student list
        print("\n--- Updated Student List ---")
        print_student_list(students)
        
        # Write updated list back to JSON file
        with open('student.json', 'w') as file:
            json.dump(students, file, indent=2)
        
        # Print success message
        print("\nStudent JSON file has been updated.")
    
    except FileNotFoundError:
        # Handle file not found error
        print("Error: File not found. Please make sure 'student.json' exists in the directory.")

if __name__ == "__main__":
    main()
