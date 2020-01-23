import os

SCORES_FILE_NAME = "Scores.txt"
ERROR_MESSAGE = "Something went wrong"


# The method calls the system and clears the console screen.
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')