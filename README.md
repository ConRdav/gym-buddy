# Gym Buddy

Gym Buddy's main goal is to support the users gym expereince. With Gym Buddy the user view a fixed workout routine, can create their own workout routine, and manage their saved workouts. When users choose to view a fixed workout they are given a three day, four day and five day option and the option they choose will be viewed on the command line. 

When Users create their own workout they can set 4 exercises and their own sets and reps to line up with their goals. Users will then get the option to view their newly created workout so they can track their progress during their workout session. 

Other Gym Buddy features the user can utilise is clearing their saved workouts in the scenario that the created workout no longer fits there fitness goals.

Gym Buddy is a Python run command line automation. The users workout data is stored in a spreadsheet run with Google Sheets which is then connected via Google Cloud and credentials are set via Google Drive. Then the Google Auth library sets up the authentication allowing the access of Gspread to update the spreadsheet.
