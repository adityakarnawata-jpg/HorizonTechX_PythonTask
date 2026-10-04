"""Task 1: Hangman Game - Horizon TechX Python Internship"""
import random

WORDS = ["python", "laptop", "internet", "program", "keyboard"]
MAX_WRONG = 6


def display_word(word, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play_hangman():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("=== HANGMAN ===")
    print(f"You have {MAX_WRONG} incorrect guesses allowed.\n")

    while wrong < MAX_WRONG:
        current = display_word(word, guessed)
        print("Word:", current)
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print("Guessed letters:", ", ".join(guessed) if guessed else "none")

        if "_" not in current:
            print(f"\nCongratulations! You guessed it: {word}")
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong += 1
            print("Wrong guess!\n")

    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        print()
