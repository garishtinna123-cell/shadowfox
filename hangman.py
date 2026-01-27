import random

# Word list with hints
words_with_hints = {
    "python": "A popular programming language",
    "computer": "An electronic device for processing data",
    "hangman": "A classic word guessing game",
    "internet": "Global network of computers",
    "keyboard": "Input device with keys"
}

# Select random word and hint
word, hint = random.choice(list(words_with_hints.items()))
guessed_letters = []
tries = 6

# Hangman visual stages
stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """
]

print("🎯 Welcome to Hangman!")
print("Hint:", hint)

while tries > 0:
    print(stages[6 - tries])

    # Display word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())

    # Check win
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        tries -= 1
        print("❌ Wrong guess! Tries left:", tries)
    else:
        print("✅ Correct guess!")

# Game over
if tries == 0:
    print(stages[-1])
    print("💀 Game Over! The word was:", word)