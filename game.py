# Authors: Hector Gonzalez
# Date: 02/05/2025
# Description:  Function to play the 'Guess the Number' game. 
#               The computer randomly selects a number between 1 and 1024, and the player has to guess it.

import random

def play_game():

    print("Welcome to the 'Guess the Number' game!")
    
    #While loop to run through the guessing game itself
    while True:
        number_to_guess = random.randint(1, 1024)  # Random number selection
        guesses = []  # List to store all guesses
        attempts = 0  # Number of attempts
        print("\nI have picked a number between 1 and 1024. Try to guess it!")
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 1024.")
                continue
            
            if guess < 1 or guess > 1024:
                print("Out of range! Please enter a number between 1 and 1024.")
                continue
            
            if guess in guesses:
                print("You already guessed that number! It won't count as an extra attempt.")
                continue
            
            guesses.append(guess)
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        
        # Display all incorrect guesses / tracker
        print("Your incorrect guesses were:", [g for g in guesses if g != number_to_guess])
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()

        