import random

def number_guesser(low=1, high=100):
    """
    A number guessing game where the user tries to guess a randomly generated number.
    The game provides feedback on whether the guess is too high or too low.

    Args:
        low (int): Lower bound of the number range (default: 1)
        high (int): Upper bound of the number range (default: 100)
    """
    secret_number = random.randint(low, high)
    attempts = 0

    print(f"\nWelcome to the Number Guesser!")
    print(f"I'm thinking of a number between {low} and {high}.")
    print("Can you guess what it is?\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                break

        except ValueError:
            print("Please enter a valid number.")

def main():
    print("NUMBER GUESSING GAME")
    print("--------------------")
    
    while True:
        print("\nSelect difficulty:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-200)")
        print("4. Custom Range")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            number_guesser(1, 50)
        elif choice == '2':
            number_guesser()
        elif choice == '3':
            number_guesser(1, 200)
        elif choice == '4':
            try:
                low = int(input("Enter lower bound: "))
                high = int(input("Enter upper bound: "))
                if low >= high:
                    print("Upper bound must be greater than lower bound.")
                    continue
                number_guesser(low, high)
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == '5':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()