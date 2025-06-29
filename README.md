
# 🎮 Hangman Game with Word Probability Visualization

This is a Python-based implementation of the classic **Hangman game** with an added twist — it visualizes the **probability of each word** from a predefined list using **Matplotlib**.

---

## 🚀 Features

- Classic text-based Hangman gameplay in the terminal
- User has **6 lives** to guess the hidden word
- Interactive guessing with real-time feedback
- Visual display of the Hangman stages as the game progresses
- Graph showing the **relative chance** of each word appearing (for illustrative purpose)

---

## 🧠 How It Works

- A word is **randomly selected** from a preset list.
- The user guesses one letter at a time.
- Incorrect guesses reduce the player's life count.
- The game ends when the user:
  - Guesses all letters correctly (**Win**)
  - Runs out of lives (**Lose**)
- After the game ends, a **Matplotlib bar plot** shows the word list, hinting at appearance probability.

---

## 📁 Project Structure

```
📦hangman-game/
 ┣ 📜 main.py               # Contains the game logic
 ┣ 📜 hangman.py            # ASCII art for different stages of hangman
 ┗ 📊 word appearance plot  # Matplotlib-based visual for word frequency
```

---

## 🧩 Requirements

- Python 3.x
- `matplotlib` library

You can install Matplotlib using:

```bash
pip install matplotlib
```

---

## ▶️ How to Run

```bash
python main.py
```

Then follow the prompts to guess letters and complete the word.

---

## 📊 Visualization

At the end of each game, a **graph** is displayed that shows:
- X-axis: Random words
- Y-axis: "Probability" (visual only, based on equal chance selection)

---

## 📌 Sample Word List

```python
["orange", "velvet", "colour", "apple", "lavender"]
```

You can modify this list to add your own words in `main.py`.

---

## 🛠️ Future Improvements

- Add real-time scoring system
- GUI version using Tkinter or PyQt
- Difficulty levels
- Word frequency from actual usage data

---

## 📄 License

This project is open-source and free to use under the MIT License.
