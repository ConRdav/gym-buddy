# Gym Buddy

Gym Buddy's main goal is to support the users gym expereince. With Gym Buddy the user view a fixed workout routine, can create their own workout routine, and manage their saved workouts. When users choose to view a fixed workout they are given a three day, four day and five day option and the option they choose will be viewed on the command line. 

When Users create their own workout they can set 4 exercises and their own sets and reps to line up with their goals. Users will then get the option to view their newly created workout so they can track their progress during their workout session. 

Other Gym Buddy features the user can utilise is clearing their saved workouts in the scenario that the created workout no longer fits there fitness goals.

Gym Buddy is a Python run command line automation. The users workout data is stored in a spreadsheet run with Google Sheets which is then connected via Google Cloud and credentials are set via Google Drive. Then the Google Auth library sets up the authentication allowing the access of Gspread to update the spreadsheet.

## Project Planning Phase

My main goal for this project was to create an application that a user can access stored workouts and create their own as it would save users using pen and paper when recording their workout routines and give them a place to store their fixed routines.

### Main Function Flow Chart

![Image](images/flowcharts/main_function_flowchart.png)

I started by planning out my main function and all the different functions that they would allow the user to run through.

### View Workout Flow Chart

![Image](images/flowcharts/view_workout_flowchart.png)

This flowchart shows my thought process on what needed to be achieved by the View Workout function. The user picks either a three day, four day or five day workout routine depending on their goals. Then the user gets to view the workout routine and the option to view another if it didn't line up with their goals or they can head back to the main function to continue navigating through the Workout Buddy.

### Create A Workout Flow Chart

![Image](images/flowcharts/create_workout_function.png)

This flowchart shows my thought process on what needed to be achieved by the Create Workout function. The user gets to name the workout, add four exercises and add the sets and reps for the workout. This allows the user a certain amount of personalisation when creating their workout.

### View Saved Workouts Flow Chart

![Image](images/flowcharts/view_saved_flowchart.png)

This function is simpler then the previous two so the flow chart is not too detailed but it allowed me to hit the specific criteria needed for the function. This allows the user to view there previously created workouts. 

### Delete Saved Workouts Flow Chart

![Image](images/flowcharts/delete_saved_flowchart.png)

This function allows the user to clear the saved workouts they have previously created.

## Features

### Welcome to Gym Buddy

On starting Gym Buddy the user is greeted to a welcome message. Below this the user has a main menu with the options to view a workout routine, create their own workout, view previous saved workouts the user have created, delete all previous saved workouts the user have created and the option to close the Gym Buddy.

![Image](images/screenshots/welcome.png)

### View A Workout Routine

Here the user gets to choose between an already made three day, four day or five day workout routine. The chosen routine is then printed out to the terminal and the user gets the option to view another routine or return to the main menu where they can continue to navigate Gym Buddy.

![Image](images/screenshots/choose_routine_1.png)

![Image](images/screenshots/choose_routine_2.png)

![Image](images/screenshots/choose_routine_3.png)

### Create A Workout

This option allows the user to create their own workout where they can personalise it by naming it setting four exercises and their sets and reps depending on their goals. When they are finished creating their own workout it is saved to the spreadsheet and the user gets the option to create a new workout, view their saved workouts or return to the main menu. 

![Image](images/screenshots/create_workout_1.png)

![Image](images/screenshots/create_workout_2.png)

### View Saved Workouts

This option allows the user to view their previously created workouts. The workouts get printed to the screen and the name, exercises, sets and reps get shown to the user. The user then is given the option to create a new workout, or return to the main menu.

![Image](images/screenshots/view_routine.png)

### Delete Saved Workouts

This option allows the user to delete all their previously created workouts giving them a clean slate to create new workouts depending on their changing workout goals. The user is then given the option to create a new workout, or return to the main menu.

![Image](images/screenshots/clear_workout.png)

### Exit Gym Buddy

This option allows closes down the Gym Buddy giving the user a thank you message and the option to restart the Gym Buddy returning to the Welcome Message on the first screen and the main menu.

![Image](images/screenshots/exit.png)

### Input Validation

All input options have validation so an error message pops up if you enter the wrong input. As shown in an example below.

![Image](images/screenshots/input_validation.png)

## Features left to implement

In the future I would like to add the ability to track workouts and enter weights used for exercise so the user can personalise their routines and follow their progress. Inlcuding estimated 1 rep max for each exercise and incrementing the weight automatically for the user would make this app more inticing for users.

## Testing

All the files pass the [PEP8](http://pep8online.com/) test successfully. As shown below.

![Image](images/screenshots/pep8.png)
