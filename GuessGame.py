import random
import Utils
import Score


# The method gets the difficulty from the user's input and return a random number between 1 to the difficulty number.
def generate_number(difficulty):
    try:
        return random.randint(1, difficulty)
    except TypeError:
        return Utils.ERROR_MESSAGE


# The method gets the difficulty level, asks from the user to guess a number and return the number the user guessed.
def get_guess_from_user(difficulty):
    guess = int(input("Guess a number between 1 to " + str(difficulty) + ": "))
    return guess


# The method gets the difficulty level and a number and compare between them. If they're equals the method
# return True. If not it will return False.
def compare_results(difficulty, secret_number):
    player_guess = get_guess_from_user(difficulty)
    if secret_number == player_guess:
        return True
    else:
        return False


# The method gets the difficulty level and uses the other methods in this file to play the full game. First,
# it will randomise a number as "generate" method does. Second, it will compare between the numbers as "compare"
# method does and finally will check if the result is True or False. If True - the method will return a message and
# add the score.
def play(difficulty):
    pc_number = generate_number(difficulty)
    result = compare_results(difficulty, pc_number)

    if result:
        print("You won the game! " + str(difficulty) + " added to your score.")
        Score.add_score(difficulty)
    else:
        print("You lose!")
