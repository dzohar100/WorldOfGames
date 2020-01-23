import random
import time
import Utils
import Score


# The method gets the difficulty level, randomise a number between 1 to 101 for "difficulty level" times (If
# difficulty is 3 there will be 3 random numbers) and return a list of the numbers. The list will be shown for 0.7
# seconds.
def generate_sequence(difficulty):
    random_numbers = []
    for i in range(difficulty):
        random_numbers.append(random.randint(1, 101))
    print(random_numbers)
    time.sleep(0.7)
    Utils.screen_cleaner()
    return random_numbers


# The method gets the difficulty level, asks from the user to guess the numbers that shown, each number separated by
# ENTER and return a list of the user's guess.
def get_list_from_user(difficulty):
    user_guess = []
    print("After seeing the numbers enter the numbers you saw, each one separated with ENTER.")
    try:
        for i in range(difficulty):
            num = int(input())
            user_guess.append(num)
        print(user_guess)
        return user_guess
    except ValueError:
        print("You can only enter numbers.")


# The method gets two lists and check if they're equals.
def is_list_equal(list_a, list_b):
    if list_a == list_b:
        return True
    else:
        return False


# The method gets the difficulty level and play the full game using the other methods in this file. First,
# it generates a sequence. Second, it will get the user's guess and finally compare the user's guess and the
# generated numbers. If the result is True, the method prints a message and add the score. If not, it will print a
# message says the user lost the game.
def play(difficulty):
    if difficulty < 1 or difficulty > 5:
        print("Difficulty level must be between 1 to 5.")
    else:
        system_number = generate_sequence(difficulty)
        user_number = get_list_from_user(difficulty)
        check_if_equal = is_list_equal(system_number, user_number)
        if check_if_equal:
            print("You won the game! You got more " + str(difficulty) + " points to your score.")
            print(system_number)
            Score.add_score(difficulty)
        elif not check_if_equal:
            print("You lose!")
            print(system_number)
        else:
            print("Error")