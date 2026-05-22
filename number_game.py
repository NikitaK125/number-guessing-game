import random
import time

# ─── AI Hint Engine ──────────────────────────────────────────────────────────

def get_ai_hint(secret, guess, attempts, low, high):
    difference = abs(secret - guess)
    range_size = high - low

    # Temperature hint (how close)
    if difference == 0:
        temperature = "🎯 EXACT!"
    elif difference <= range_size * 0.05:
        temperature = "🔥 Burning hot!"
    elif difference <= range_size * 0.10:
        temperature = "♨️  Very warm!"
    elif difference <= range_size * 0.20:
        temperature = "🌡️  Warm"
    elif difference <= range_size * 0.35:
        temperature = "🌤️  Lukewarm"
    elif difference <= range_size * 0.50:
        temperature = "❄️  Cold"
    else:
        temperature = "🧊 Freezing cold!"

    # Direction hint
    if guess < secret:
        direction = "📈 Go HIGHER"
    elif guess > secret:
        direction = "📉 Go LOWER"
    else:
        direction = "✅ That's it!"

    # Smart range narrowing hint
    if guess < secret:
        new_low = guess
        new_high = high
    else:
        new_low = low
        new_high = guess

    smart_hint = f"🤖 AI: Try between {new_low} and {new_high}"

    # Encouragement based on attempts
    if attempts == 1:
        encouragement = "💪 Great start!"
    elif attempts <= 3:
        encouragement = "🧠 You're thinking smart!"
    elif attempts <= 5:
        encouragement = "🎲 Keep going, you're getting there!"
    elif attempts <= 7:
        encouragement = "😅 Don't give up!"
    else:
        encouragement = "🤔 Think carefully..."

    return temperature, direction, smart_hint, encouragement


def get_difficulty():
    difficulties = {
        "1": ("Easy",   1,   50,  10),
        "2": ("Medium", 1,  100,   7),
        "3": ("Hard",   1,  200,   5),
        "4": ("Expert", 1, 1000,   8),
    }

    print("\n🎮 Choose Difficulty:")
    print("  1 → Easy    (1–50,   10 attempts)")
    print("  2 → Medium  (1–100,   7 attempts)")
    print("  3 → Hard    (1–200,   5 attempts)")
    print("  4 → Expert  (1–1000,  8 attempts)")

    while True:
        choice = input("\nYour choice (1-4): ").strip()
        if choice in difficulties:
            return difficulties[choice]
        print("⚠️  Please enter 1, 2, 3, or 4")


def calculate_score(attempts, max_attempts, time_taken, difficulty_name):
    base_score = 1000
    attempt_penalty = (attempts - 1) * 80
    time_penalty = int(time_taken * 2)

    difficulty_bonus = {
        "Easy": 0,
        "Medium": 200,
        "Hard": 500,
        "Expert": 1000,
    }.get(difficulty_name, 0)

    score = max(0, base_score - attempt_penalty - time_penalty + difficulty_bonus)
    return score


def display_progress_bar(attempts, max_attempts):
    used = attempts
    remaining = max_attempts - used
    bar = "🟥" * used + "🟩" * remaining
    print(f"  Attempts: [{bar}] {used}/{max_attempts}")


# ─── Main Game ───────────────────────────────────────────────────────────────

def play_game():
    diff_name, low, high, max_attempts = get_difficulty()
    secret = random.randint(low, high)
    attempts = 0
    current_low = low
    current_high = high
    start_time = time.time()
    guess_history = []

    print(f"\n{'='*50}")
    print(f"  🎮 {diff_name} Mode — Guess the number!")
    print(f"  Range: {low} to {high}  |  Max attempts: {max_attempts}")
    print(f"{'='*50}\n")

    while attempts < max_attempts:
        display_progress_bar(attempts, max_attempts)

        try:
            raw = input(f"  Your guess ({current_low}–{current_high}): ").strip()

            if raw.lower() == "quit":
                print(f"\n😔 You quit! The number was {secret}")
                return False, 0

            guess = int(raw)

            if guess < low or guess > high:
                print(f"⚠️  Please guess between {low} and {high}\n")
                continue

        except ValueError:
            print("⚠️  Please enter a valid number\n")
            continue

        attempts += 1
        guess_history.append(guess)

        if guess == secret:
            time_taken = time.time() - start_time
            score = calculate_score(attempts, max_attempts, time_taken, diff_name)

            print(f"\n{'='*50}")
            print(f"  🎉 CORRECT! The number was {secret}!")
            print(f"  ✅ Solved in {attempts} attempt(s)")
            print(f"  ⏱️  Time: {time_taken:.1f} seconds")
            print(f"  🏆 Score: {score} points")
            print(f"  📊 Your guesses: {' → '.join(map(str, guess_history))}")
            print(f"{'='*50}\n")
            return True, score

        # AI Hints
        temperature, direction, smart_hint, encouragement = get_ai_hint(
            secret, guess, attempts, current_low, current_high
        )

        # Update narrowed range
        if guess < secret:
            current_low = max(current_low, guess)
        else:
            current_high = min(current_high, guess)

        remaining = max_attempts - attempts
        print(f"\n  {temperature}  {direction}")
        print(f"  {smart_hint}")
        print(f"  {encouragement}")
        print(f"  ⏳ {remaining} attempt(s) remaining\n")

    # Game over
    time_taken = time.time() - start_time
    print(f"\n{'='*50}")
    print(f"  💀 GAME OVER! You ran out of attempts!")
    print(f"  The number was: {secret}")
    print(f"  📊 Your guesses: {' → '.join(map(str, guess_history))}")
    print(f"{'='*50}\n")
    return False, 0


# ─── Game Loop ────────────────────────────────────────────────────────────────

def run():
    print("=" * 50)
    print("   🎮 Number Guessing Game with AI Hints")
    print("   Can you guess the number?")
    print("=" * 50)

    total_score = 0
    games_played = 0
    games_won = 0

    while True:
        won, score = play_game()
        games_played += 1
        total_score += score

        if won:
            games_won += 1
            print(f"🏆 Running total score: {total_score} points")

        play_again = input("🔄 Play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            break

    # Final stats
    print(f"\n{'='*50}")
    print(f"  📊 Final Stats")
    print(f"  Games Played : {games_played}")
    print(f"  Games Won    : {games_won}")
    if games_played > 0:
        win_rate = (games_won / games_played) * 100
        print(f"  Win Rate     : {win_rate:.0f}%")
    print(f"  Total Score  : {total_score} points")
    print(f"{'='*50}")
    print("  Thanks for playing! 👋\n")


# ─── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run()
