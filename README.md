# 📚 VocabPoP — German Flashcard App

VocabPoP is a simple and interactive flashcard application that helps you memorize the 1000 most basic German words. Built using Python's `tkinter` for the GUI and `pandas` for data handling, this app tracks your progress and lets you visually flip cards to learn German vocabulary.

---

## 🚀 Features

- Displays flashcards with German words and reveals the English translation after 3 seconds.
- Allows users to mark words as "learned" by clicking a check button.
- Tracks the number of words you’ve memorized across sessions.
- Automatically disables buttons and congratulates the user after reaching the goal.
- Saves progress to a CSV file (`words_learned.csv`).

---

## 🧠 How It Works

1. **Loads Words**: Reads German-English word pairs from `german_words.csv`.
2. **Tracks Progress**: Reads and updates `words_learned.csv` to track learned words.
3. **Timed Flip**: Shows the English translation after 3 seconds.
4. **Completion**: When all 1000 words are marked as learned, a congratulatory message is shown and the app disables further input.

✨ To Do / Future Improvements
Add support for other languages.

Allow resetting progress from the UI.

Add audio pronunciation for words.

Make total word limit configurable (currently hardcoded as 1000).
