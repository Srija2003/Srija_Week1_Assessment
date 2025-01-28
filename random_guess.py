import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too Low! Try again.")
            elif user_guess > number_to_guess:
                print("Too High! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print("Thanks for playing!")

number_guessing_game()
