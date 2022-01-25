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

three = SHEET.worksheet('three')
four = SHEET.worksheet('four')
five = SHEET.worksheet('five')
workouts = SHEET.worksheet('workouts')

data1 = three.get_all_values()
data2 = four.get_all_values()
data3 = five.get_all_values()
data4 = workouts.get_all_values()
print(data1)
print(data2)
print(data3)
print(data4)