import re
from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gym-buddy')

three_day = SHEET.worksheet('three')
four_day = SHEET.worksheet('four')
five_day = SHEET.worksheet('five')
workouts = SHEET.worksheet('workouts')


def get_workout_routine():
    """
    Gets the workout routine requested by the user
    """
    print("Please choose a workout routine.")
    print("To view a 3 day routine press 3.")
    print("To view a 4 day routine press 4.")
    print("To view a 5 day routine press 5.\n")
    routine = input("Enter your choice here: ")
    validate_input(routine)
    show_routine(routine)
    print("To view another workout routine enter 1.")
    print("To return to the main menu enter 2.\n")
    create_choice = input("Enter 1 or 2: \n")
    if validate_input(create_choice):
        user_choice(create_choice)
    else:
        print("Invalid entry, please enter 1 or 2.")


def validate_input(value):
    """
    input validation
    """
    pattern = re.compile('[1-5]{1}')
    return pattern.match(value)


def show_routine(routine):
    """
    prints user requested routine
    """
    if routine == '3':
        print(f"You picked the {routine} day workout routine.\n")
        pprint(three_day.get_all_records())
    elif routine == '4':
        print(f"You picked the {routine} day workout routine.\n")
        pprint(four_day.get_all_records())
    elif routine == '5':
        print(f"You picked the {routine} day workout routine.\n")
        pprint(five_day.get_all_records())
    else:
        print("Invalid entry, please enter 3, 4 or 5.")
        get_workout_routine()


def get_input(prompt="", cast=None, condition=None, error_message=None):
    """
    Input validation
    """
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except ValueError:
            print(error_message or "Invalid input. Try again.")


def create_own_workout():
    """
    Allows user to create own workout
    """
    print("Create your own workout.\n")
    new_workout = get_input(prompt="Name your workout: ")
    print("You are limited to 4 exercises to pick carefully!\n")
    create_exercise1 = get_input(prompt="Enter your exercise name: ")
    create_exercise2 = get_input(prompt="Enter your exercise name: ")
    create_exercise3 = get_input(prompt="Enter your exercise name: ")
    create_exercise4 = get_input(prompt="Enter your exercise name: \n")
    print("Now enter the workouts sets and reps.")
    print("You are limited to numbers 1-9.\n")
    create_sets = get_input(prompt="Enter the amount of sets per exercise: ",
                            cast=int)
    create_reps = get_input(prompt="Enter the amount of reps per exercise: ",
                            cast=int)
    print("Well done you have created your own workout!\n")
    data = [[new_workout, create_exercise1, create_exercise2, create_exercise3,
            create_exercise4, create_sets, create_reps]]
    save_workouts(data)

    print("Enter 1 to view saved workouts.")
    print("Enter 2 to create a new workout.")
    print("Enter 3 to return to the main menu.\n")
    create_choice = input("Enter 1, 2 or 3: \n")
    if validate_input(create_choice):
        user_choice(create_choice)
    else:
        print("Invalid entry, please enter 1, 2 or 3.")


def save_workouts(data):
    """
    updates the workouts worksheet
    """
    print("Saving workout...\n")
    workouts.append_rows(data)
    print("Workout has been saved succesfully.\n")


def view_saved_workouts():
    """
    shows all saved workouts created by user
    """
    pprint(workouts.get_all_records())


def user_choice(create_choice):
    """
    gives user choice feedback
    """
    if create_choice == '1':
        view_saved_workouts()
    elif create_choice == '2':
        create_own_workout()
    else:
        main()


def clear_saved_workouts():
    """
    clears all saved workouts
    """
    print("Are you sure you want to remove all saved workouts?")
    print("Enter 1 for Yes.")
    print("Enter 2 for No.")
    clear_choice = input("Enter your choice here: ")
    validate_input(clear_choice)
    if clear_choice == '1':
        print("Removing saved workouts...")
        workouts.clear()
        print("Saved workouts removed.")
    elif clear_choice == '2':
        print("Returning to main menu")
        main()
    else:
        print("Invalid entry, please enter 1 or 2.\n")
        clear_saved_workouts()


def main():
    """
    runs the app
    """
    print("""
===============================
To view a routine press 1.

To create own workout press 2.

To view saved workouts press 3.

To clear saved workouts press 4.
================================
    """)
    main_choice = input("Enter your choice here: ")
    validate_input(main_choice)
    if main_choice == '1':
        get_workout_routine()
    elif main_choice == '2':
        create_own_workout()
    elif main_choice == '3':
        view_saved_workouts()
    elif main_choice == '4':
        clear_saved_workouts()
    else:
        print("Invalid entry, please enter 1, 2, 3 or 4.")


print("""
=========================

WELCOME TO THE GYM BUDDY

=========================
""")
main()
