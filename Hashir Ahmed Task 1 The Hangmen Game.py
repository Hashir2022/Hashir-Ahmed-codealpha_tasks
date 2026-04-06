import random

# List of 5 predefined words
words = ["apple", "chair", "tiger", "plant", "bread"]

# Randomly select a word
word = random.choice(words)

# Initialize variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while incorrect_guesses < max_attempts:

    # Display current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Take input
    guess = input("Enter a letter: ").strip().lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter!")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check correct or wrong
    if guess in word:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong! Attempts left:", max_attempts - incorrect_guesses)

# Lose condition
if incorrect_guesses == max_attempts:
    print("💀 Game Over! The word was:", word)