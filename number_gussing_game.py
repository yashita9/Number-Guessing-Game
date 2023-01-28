# choosing the random number between 1 to 100
# make function to set the difficulty
# let the user guess the number
# function to check the users guess against actual answer
# track the numbers to turns and reduce by 1 if they get it wrong
# repeat the guessing functionality if they get it wrong

from random import randint

EASY_LEVELTURNS = 10  # global variable
HARD_LEVEL_TURNS = 5  # global variable


def check_answer(guess, answer, turns):
    """Checks ans against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print("You guessed it right! You win!")


def set_difficulty():
    level = input("Choose a difficulty. easy or hard: ")
    if level == "easy":
        return EASY_LEVELTURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcom tothe guessing game")
    print("I am thinking of a number between 1 to 100")

    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses, you loose!")
            return


game()
