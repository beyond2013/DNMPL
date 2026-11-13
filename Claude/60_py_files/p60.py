"""Problem 60: Number-guessing game (scripted demo)"""

import random


def guessing_game(secret, scripted_guesses=None, max_attempts=7):
    """Play with input() if scripted_guesses is None, else use the list."""
    attempts = 0
    guesses = iter(scripted_guesses) if scripted_guesses is not None else None
    while attempts < max_attempts:
        raw = next(guesses, None) if guesses else input("Your guess (1-100): ")
        if raw is None:
            break
        guess = int(raw)
        attempts += 1
        if guess == secret:
            print(f"Correct! You needed {attempts} attempt(s).")
            return True
        print(f"{guess}: too {'low' if guess < secret else 'high'}.")
    print(f"Out of attempts. The number was {secret}.")
    return False


def p60():
    secret = random.randint(1, 100)
    print("(Demo: binary-search strategy against a random secret)")
    low, high, guesses = 1, 100, []
    # Precompute a binary-search sequence of guesses for the demo
    while low <= high:
        mid = (low + high) // 2
        guesses.append(mid)
        if mid == secret:
            break
        low, high = (mid + 1, high) if mid < secret else (low, mid - 1)
    guessing_game(secret, guesses)


if __name__ == "__main__":
    p60()
