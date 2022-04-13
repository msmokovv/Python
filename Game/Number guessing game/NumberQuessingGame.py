import random
def user_guess(num, max_num_guesses=10):
    for _ in range(max_num_guesses):
        guess = int(input("Guess a number between 1 and 100: "))
        print("Your guess was {}".format(guess))

        if guess < num:
            print("Your guess was too low: guess again!")
        elif guess > num:
            print("Your guess was too high: guess again!")
        elif guess == num:
            print("Correct! Well done!")
            return

    print("Sorry, you ran out of guesses.")


if __name__ == '__main__':
    while True:
        user_guess(random.randint(1, 100))

        again = input("Would you like to play again? (Y or N): ")
        if again.lower() != "y":
            print("Ok, goodbye")
            break
