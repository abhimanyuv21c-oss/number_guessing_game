import random

def number_guessing_game():
    print("🎉 Welcome to the Number Guessing Game!")
    print("=======================================")
    print("Rules:")
    print("👉 I will randomly pick a number between 1 and 100.")
    print("👉 You need to guess the number based on difficulty level.")
    print("👉 I'll guide you if your guess is too high or too low.")
    print("👉 You win if you guess the number within the given chances!")
    print("=======================================\n")

    # Difficulty level selection
    difficulty = input("Choose a difficulty (easy/medium/hard): ").strip().lower()
    
    if difficulty == "easy":
        chances = 10
    elif difficulty == "medium":
        chances = 7
    elif difficulty == "hard":
        chances = 5
    else:
        print("Invalid choice! Defaulting to medium difficulty.")
        chances = 7

    # Computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempt = 0

    print(f"\nI have chosen a number between 1 and 100. You have {chances} chances to guess it!")

    while attempt < chances:
        try:
            guess = int(input(f"Attempt {attempt+1}/{chances} - Enter your guess: "))
        except ValueError:
            print("⚠ Invalid input! Please enter a number between 1 and 100.")
            continue

        attempt += 1

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempt} attempts!")
            break
        elif guess < number_to_guess:
            print("📉 Too low! Try a higher number.")
        else:
            print("📈 Too high! Try a lower number.")

        remaining = chances - attempt
        if remaining > 0:
            print(f"⏳ You have {remaining} chances left.\n")

    else:
        print(f"😢 Sorry, you've used all {chances} chances. The number was {number_to_guess}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
