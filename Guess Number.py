import random

def guess_the_number():
    secret_number = random.randint(1, 100)  # Generates a random number between 1 and 100
    attempts = 0  # Initialize the number of attempts to 0

    print("Welcome to the Guess the Number game!")
    print("I've selected a random number between 1 and 100. Try to guess it.")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1  # Increase the number of attempts with each guess

            if user_guess < secret_number:
                print("Too low! Try a higher number.")
            elif user_guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop when the correct number is guessed
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
