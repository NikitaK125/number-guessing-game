# 🎮 Number Guessing Game with AI Hints

A fun Python game where you guess a secret number — with an **AI hint engine** that guides you using temperature clues, smart range narrowing, and encouragement!

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 💻 Demo

```
==================================================
   🎮 Number Guessing Game with AI Hints
==================================================

🎮 Choose Difficulty:
  1 → Easy    (1–50,   10 attempts)
  2 → Medium  (1–100,   7 attempts)
  3 → Hard    (1–200,   5 attempts)
  4 → Expert  (1–1000,  8 attempts)

Your choice: 2

==================================================
  🎮 Medium Mode — Guess the number!
  Range: 1 to 100  |  Max attempts: 7
==================================================

  Attempts: [🟩🟩🟩🟩🟩🟩🟩] 0/7
  Your guess (1–100): 50

  ♨️  Very warm!  📈 Go HIGHER
  🤖 AI: Try between 50 and 100
  🧠 You're thinking smart!
  ⏳ 6 attempt(s) remaining

  Your guess (50–100): 75

  🔥 Burning hot!  📉 Go LOWER
  🤖 AI: Try between 50 and 75
  🧠 You're thinking smart!
  ⏳ 5 attempt(s) remaining

  Your guess (50–75): 73

  🎉 CORRECT! The number was 73!
  ✅ Solved in 3 attempt(s)
  ⏱️  Time: 12.4 seconds
  🏆 Score: 1034 points
  📊 Your guesses: 50 → 75 → 73
```

---

## ✨ Features

- 🤖 **AI Hint Engine** — temperature clues (🔥 hot / 🧊 freezing)
- 📉 **Smart range narrowing** — AI tells you the updated range after each guess
- 🎯 **4 difficulty levels** — Easy, Medium, Hard, Expert
- 🏆 **Scoring system** — based on attempts, time, and difficulty
- 📊 **Visual progress bar** — see your remaining attempts
- 📈 **Guess history** — track all your guesses
- 📊 **Final stats** — win rate, total score across games
- ✅ Zero external dependencies

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/number-guessing-game.git

# Navigate into folder
cd number-guessing-game

# Run the game
python number_game.py
```

---

## 🧪 Run Tests

```bash
python test_number_game.py
```

---

## 📁 Project Structure

```
number-guessing-game/
│
├── number_game.py         # Main game logic
├── test_number_game.py    # Unit tests
├── requirements.txt       # Dependencies (none!)
└── README.md              # You are here
```

---

## 🏆 Scoring System

| Factor | Effect |
|---|---|
| Each extra attempt | -80 points |
| Time taken | -2 pts/sec |
| Medium difficulty | +200 bonus |
| Hard difficulty | +500 bonus |
| Expert difficulty | +1000 bonus |

---

## 🌡️ AI Temperature Hints

| Hint | Meaning |
|---|---|
| 🔥 Burning hot | Within 5% of the range |
| ♨️ Very warm | Within 10% |
| 🌡️ Warm | Within 20% |
| 🌤️ Lukewarm | Within 35% |
| ❄️ Cold | Within 50% |
| 🧊 Freezing | More than 50% away |

---

## 🌱 Future Improvements

- [ ] Add a leaderboard (save high scores to a file)
- [ ] Multiplayer mode (two players take turns)
- [ ] GUI version using Tkinter
- [ ] Timed challenge mode

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Made with ❤️ and Python by **YOUR_NAME**  
⭐ Star this repo if you found it helpful!
