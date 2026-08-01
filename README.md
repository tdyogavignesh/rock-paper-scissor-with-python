# Rock, Paper, Scissors Game 🪨 📄 ✂️

A lightweight, interactive command-line console game built entirely in Python. Play continuous rounds against an AI opponent while tracking scores in real time.

## ✨ Features
* **Typo Protection:** Automatically handles inputs with mixed capitalization or accidental leading/trailing spaces using `.lower().strip()`.
* **Score Keeping:** Displays updated point scores for both the player and the computer instantly after every single round.
* **Smart Game Loop:** Gracefully handles continuous gameplay loop resets without repeating computer weapon choices.

## 🚀 Getting Started

### Prerequisites
You need Python 3 installed on your machine. You can verify your version by running:
```bash
python --version
```

### Installation & Running the Game
1. Clone your repository down to your computer:
   ```bash
   git clone https://github.com
   ```
2. Navigate directly into the project directory:
   ```bash
   cd YOUR-REPOSITORY-NAME
   ```
3. Boot up the script:
   ```bash
   python main.py
   ```

## 🎮 How to Play
1. Type `rock`, `paper`, or `scissor` into the prompt.
2. The game validates your input and reveals the computer's randomized pick.
3. Points are awarded based on traditional victory rules:
   * **Paper** covers **Rock**
   * **Rock** smashes **Scissor**
   * **Scissor** cuts **Paper**
4. Type `yes` when prompted to play another round, or type any other key to view your final scoreboard and exit.

## 🛠️ Built With
* **Python 3** - Underlying programming language.
* **Random Module** - Native Python standard library handling computer path options.

## 📄 License
This project is open-source and free to modify under the MIT License.
