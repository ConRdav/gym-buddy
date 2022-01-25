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
        print("Please choose your preferred routine by entering 3, 4 or 5.\n")

        routine = input("Enter your choice here: ")
        if validate_routine(routine):
            print(f"You picked the {routine} day workout routine.")
            break
        else:
            print("Invalid entry, please enter 3, 4 or 5.")

    show_routine(routine)


def validate_routine(routine):
    """
    validates the user input
    """
    pattern = re.compile('[3-5]{1}')
    return pattern.match(routine)


def show_routine(routine):
    """
    prints user requested routine
    """
    if routine == '3':
        pprint(three_day.get_all_values())
    elif routine == '4':
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

