import Utils
import MemoryGame
import GuessGame


# The method gets a name and return a "Welcome" message using the user's name.
def welcome(name):
    print("Hello, " + name + " and welcome to the World Of Games (WoG). \nHere you can find many cool games to play")


# The method asks from the user to choose a game by a number and then choose a difficulty level and start the chosen
# game with the difficulty level chosen by the user.
def load_game():
    print("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you "
          "have to guess it back. \n 2. Guess Game - guess a number and see if you chose like the computer")
    error = Utils.ERROR_MESSAGE
    try:
        chosen_game = int(input())
        while chosen_game != 1 and chosen_game != 2:
            print(error + " - You have two options only (1 or 2).")
            chosen_game = int(input())
        print("Please choose game difficulty from 1 to 5:")
        game_dif = int(input())
        while game_dif < 1 or game_dif > 5:
            print(error + " - Game difficulty must be between 1 to 5.")
            game_dif = int(input())
        if chosen_game == 1:
            MemoryGame.play(game_dif)
        elif chosen_game == 2:
            GuessGame.play(game_dif)
    except (ValueError, UnboundLocalError):
        print(error + " - You must enter numbers only.")
