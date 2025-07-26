import random
import string

# ---------------------------------------------------------------------------
# 1. Configuration
# ---------------------------------------------------------------------------
WORDS = ["python", "guitar", "planet", "garden", "rocket"]  # 5 predefined words
MAX_WRONG = 6                                              # allowed wrong guesses

# ---------------------------------------------------------------------------
# 2. Helper functions
# ---------------------------------------------------------------------------
def choose_word() -> str:
    """Return a random secret word from WORDS."""
    return random.choice(WORDS)

def display_progress(secret: str, guesses: set[str]) -> str:
    """Return the secret word with unguessed letters shown as '_'."""
    return " ".join(c if c in guesses else "_" for c in secret)

def get_guess(already_guessed: set[str]) -> str:
    """Prompt the user for a single new letter and validate it."""
    while True:
        guess = input("Pick a letter: ").lower().strip()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("❗  Please enter a single alphabetic character (A‑Z).")
        elif guess in already_guessed:
            print("⚠️  You already tried that letter.")
        else:
            return guess

# ---------------------------------------------------------------------------
# 3. Main game logic
# ---------------------------------------------------------------------------
def play():
    secret = choose_word()
    guessed: set[str] = set()
    wrong = 0

    print("\n=== Hangman ===")
    while wrong < MAX_WRONG and set(secret) - guessed:
        print(f"\nWord:  {display_progress(secret, guessed)}")
        print(f"Wrong: {wrong}/{MAX_WRONG}")
        guess = get_guess(guessed)

        guessed.add(guess)

        if guess in secret:
            print("✅  Good guess!")
        else:
            wrong += 1
            print("❌  Nope!")

    # -----------------------------------------------------------------------
    # 4. Game result
    # -----------------------------------------------------------------------
    if wrong < MAX_WRONG:
        print(f"\n🎉 You won! The word was {secret.upper()}.")
    else:
        print(f"\n💀 You lost. The word was {secret.upper()}.")

# ---------------------------------------------------------------------------
# 5. Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    play()
