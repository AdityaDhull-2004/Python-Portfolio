import random
a = random.randint(1,101)


print("Welcome to the number guessing game ")


def play():
    difficulty = input("Enter the difficulty level of the game. 'Easy', 'Medium' or 'Hard'.\n")
    guess = 0
    
    
    
    if difficulty == "easy":
        print("You have 10 guesses to guess a number from 1 to 100 ")
        no_of_easy_guesses = 0
        while guess != a and no_of_easy_guesses <= 9:
            print(f"Number of guesses left = {10 - no_of_easy_guesses}")
            guess = int(input("guess a nmber from 1 to 100.\n"))
            if guess < a:
                print("The number is larger than your guess. ")
            elif guess > a:
                print("The number is smaller than your guess. ")
            else:
                print("You guessed the right number. ")
                return
            no_of_easy_guesses += 1


    elif difficulty == "medium":
        print("You have 7 guesses to guess a number from 1 to 100 ")
        no_of_medium_guesses = 0
        while guess != a and no_of_medium_guesses <= 6:
            print(f"Number of guesses left = {7 - no_of_medium_guesses}")
            guess = int(input("guess a nmber from 1 to 100.\n"))
            if guess < a:
                print("The number is larger than your guess. ")
            elif guess > a:
                print("The number is smaller than your guess. ")
            else:
                print("You guessed the right number. ")
                return
            no_of_medium_guesses += 1


    elif difficulty == "hard":
        print("You have 5 guesses to guess a number from 1 to 100 ")
        no_of_hard_guesses = 0
        while guess != a and no_of_hard_guesses <= 4:
            print(f"Number of guesses left = {5 - no_of_hard_guesses}")
            guess = int(input("guess a nmber from 1 to 100.\n"))
            if guess < a:
                print("The number is larger than your guess. ")
            elif guess > a:
                print("The number is smaller than your guess. ")
            else:
                print("You guessed the right number. ")
                return
            no_of_hard_guesses += 1
            

    else:
        print("please enter a valid input, ")
        play()


play()