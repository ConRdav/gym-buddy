from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials

# Global variables defined to enable project access to Google Sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gym-buddy')

# Specific worksheets defined as global variables to refine code
three_day = SHEET.worksheet('three')
four_day = SHEET.worksheet('four')
five_day = SHEET.worksheet('five')
workouts = SHEET.worksheet('workouts')


def get_workout_routine():
    """
    Returns a pre-defined workout routine requested by the user,
    based on the number of times they wish to workout per week.
    """
    print("""
========================================
Please choose a workout routine.

To view a 3 day routine press 3.

To view a 4 day routine press 4.

To view a 5 day routine press 5.
========================================
""")
    routine = input("Enter your choice here:\n")
    show_routine(routine)
    print("""
========================================
To view another workout routine enter 1.

To return to the main menu enter 2.

To exit the Gym Buddy enter 3.
========================================
""")
    while input != 1 or 2 or 3:
        choice = input("Enter 1, 2 or 3:\n")
        if choice == '1':
            get_workout_routine()
        elif choice == '2':
            main()
        elif choice == '3':
            exit_app()
        else:
            print("Invalid entry, please enter 1, 2 or 3.")


def show_routine(routine):
    """
    Prints the pre-defined workout routine based on the input of the user.
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
    Validates input and handles value error exceptions.
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
    Allows user to create their own personalised workout
    and save it to a worksheet for future reference.
    """
    print("Create your own workout.\n")
    new_workout = get_input(prompt="Name your workout:\n")
    print("You are limited to 4 exercises to pick carefully!\n")
    create_exercise1 = get_input(prompt="Enter your exercise name:\n")
    create_exercise2 = get_input(prompt="Enter your exercise name:\n")
    create_exercise3 = get_input(prompt="Enter your exercise name:\n")
    create_exercise4 = get_input(prompt="Enter your exercise name:\n")
    print("Now enter the workouts sets and reps.")
    print("You are limited to numbers 1-9.\n")
    create_sets = get_input(prompt="Enter the amount of sets per exercise:\n",
                            cast=int)
    create_reps = get_input(prompt="Enter the amount of reps per exercise:\n",
                            cast=int)
    print("Well done you have created your own workout!\n")
    data = [[new_workout, create_exercise1, create_exercise2, create_exercise3,
            create_exercise4, create_sets, create_reps]]
    save_workouts(data)
    print("""
========================================
Enter 1 to view saved workouts.

Enter 2 to create a new workout.

Enter 3 to return to the main menu.

Enter 4 to exit the Gym Buddy.
========================================
""")
    while input != 1 or 2 or 3 or 4:
        choice = input("Enter 1, 2, 3 or 4:\n")
        if choice == '1':
            view_saved_workouts()
        elif choice == '2':
            create_own_workout()
        elif choice == '3':
            main()
        elif choice == '4':
            exit_app()
        else:
            print("Invalid entry, please enter 1, 2, 3 or 4.")


def save_workouts(data):
    """
    Saves the user's created workout by appending it to the workout worksheet.
    """
    print("Saving workout...\n")
    workouts.append_rows(data)
    print("Workout has been saved succesfully.\n")


def view_saved_workouts():
    """
    Displays all saved workouts created by user for their reference.
    """
    pprint(workouts.get_all_records())
    print("""
========================================
To return to the main menu press 1.

To exit the Gym Buddy press 2.
========================================
""")
    while input != 1 or 2:
        choice = input("Enter 1 or 2:\n")
        if choice == '1':
            main()
        elif choice == '2':
            exit_app()
        else:
            print("Invalid entry, please enter 1 or 2.")


def clear_saved_workouts():
    """
    Clears all saved workouts from the worksheet.
    """
    print("Are you sure you want to remove all saved workouts?\n")
    print("Enter 1 for Yes.")
    print("Enter 2 for No.")
    choice = input("Enter your choice here:\n")
    if choice == '1':
        print("Removing saved workouts...")
        workouts.batch_clear(["2:50"])
        print("Saved workouts removed.")
        main()
    elif choice == '2':
        print("Returning to main menu...")
        main()
    else:
        print("Invalid entry, please enter 1 or 2.\n")
        clear_saved_workouts()


def main():
    """
    Runs the app and loads the main menu for ease of navigation.
    """
    print("""
========================================
To view a routine press 1.

To create own workout press 2.

To view saved workouts press 3.

To clear saved workouts press 4.

To exit the Gym Buddy press 5.
========================================
    """)
    while input != 1 or 2 or 3 or 4 or 5:
        choice = input("Enter your choice here:\n")
        if choice == '1':
            get_workout_routine()
        elif choice == '2':
            create_own_workout()
        elif choice == '3':
            view_saved_workouts()
        elif choice == '4':
            clear_saved_workouts()
        elif choice == '5':
            exit_app()
        else:
            print("Invalid entry, please enter 1, 2, 3, 4 or 5.")


def exit_app():
    """
    Exits the app and takes user to the welcome screen.
    """
    print("""
========================================

Thanks for using the Gym Buddy!

========================================
""")
    while input != 1 or 2:
        restart = input("To restart the Gym Buddy enter 1:\n")
        if restart == '1':
            print("""
========================================

    WELCOME TO THE GYM BUDDY

========================================
""")
            main()
        else:
            print("Invalid entry, please enter 1.")


print("""
========================================

    WELCOME TO THE GYM BUDDY

========================================
""")
main()
