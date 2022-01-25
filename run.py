import gspread
from google.oauth2.service_account import Credentials
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
    print("Please choose a workout routine.")
    print("Your options are a 3 day, 4 day or 5 day routine.")
    print("Please choose your preferred routine by entering 3, 4 or 5.\n")
    routine = input("Enter your choice here: ")
    show_routine(routine)


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


get_workout_routine()
