import gspread
from google.oauth2.service_account import Credentials
import re
from pprint import pprint


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
    while True:
        print("Please choose a workout routine.")
        print("Your options are a 3 day, 4 day or 5 day routine.")
        print("Please choose your preferred routine by entering 1, 2 or 3.\n")

        routine = input("Enter your choice here: ")
        if validate_input(routine):
            print(f"You picked the {routine} day workout routine.")
            break
        else:
            print("Invalid entry, please enter 1, 2 or 3.")

    show_routine(routine)


def validate_input(value):
    """
    input validation
    """
    pattern = re.compile('[1-3]{1}')
    return pattern.match(value)


def show_routine(routine):
    """
    prints user requested routine
    """
    if routine == '1':
        pprint(three_day.get_all_values())
    elif routine == '2':
        pprint(four_day.get_all_values())
    else:
        pprint(five_day.get_all_values())


def get_input(prompt="", cast=None, condition=None, errorMessage=None):
    """
    Input validation
    """
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except ValueError:
            print(errorMessage or "Invalid input. Try again.")


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
    create_exercise4 = get_input(prompt="Enter your exercise name: ")
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
    pprint(workouts.get_all_values())


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


def main():
    """
    runs the app
    """
    print("To view a routine press 1.\n")
    print("To create own workout press 2.\n")
    print("To view saved workouts press 3.\n")
    main_choice = input("Enter your choice here: ")
    validate_input(main_choice)
    if main_choice == '1':
        get_workout_routine()
    elif main_choice == '2':
        create_own_workout()
    else:
        view_saved_workouts()


print("Welcome to the Gym Buddy!\n")
main()
