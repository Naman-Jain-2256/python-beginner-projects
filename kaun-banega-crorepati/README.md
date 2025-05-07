# Kaun Banega Crorepati (KBC) Python Quiz Game 🎮

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Status](https://img.shields.io/badge/Status-improving-blue.svg)

Welcome to the "Kaun Banega Crorepati" (KBC) Python quiz game! 🏆 This is a simple terminal-based quiz game that mimics the famous Indian television show "Kaun Banega Crorepati." The game allows users to answer multiple-choice questions and win virtual money 💰 based on their performance. The game includes a feature to quit at any time.

---

## Features ✨

- 10 randomized multiple-choice questions (A-D). 🎓
- Clean input handling with support for lowercase and uppercase. 🧠
- Graceful exit anytime using `quit` to retain your winnings. 🚪💰
- Safe-level at Rs. 10,000 ensures minimum winnings after question 5. 🛡️
- Interactive flow with answer checking and correct answer display. ✅❌
- Final congratulatory message if all answers are correct. 🥳

---

## How to Play 🎮

1. Run the Python script `kbc_game.py` in your terminal. 💻
2. Answer the questions by typing A, B, C, or D. 🅰️🅱️🅾️🅾️
3. If you get a question wrong, you lose the game, and your total money is displayed. ❌💵
4. If you want to quit anytime, type 'quit', and you will keep the money you have earned so far. 🚪💸

## Requirements 📜

- Python 3.12 🐍

## How to Run 🚀

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/beginner-python-projects.git
    cd beginner-python-projects
    cd kaun-banega-crorepati
    ```

2. Run the script `kbc_game.py`.

    ```bash
    python kaun-banega-crorepati.py
    ```

3. Play and enjoy the game! 🎉

## Example Gameplay 🎮

```bash
  ********** WELCOME TO KAUN BANEGA CROREPATI **********
   

************************************************************
Question for Rs.1000
 
(to quit type 'quit' and you will retain the money you won)
1.) India is a part of which continent?
Option-A) Asia         Option-B) Africa
Option-C) Antarctica         Option-D) North America
Enter ans (A-D): 
=> a
Checking your answer...
Correct! 🎉

Loading next question...

************************************************************
Question for Rs.2000

(to quit type 'quit' and you will retain the money you won)
2.) Which is the largest ocean in the world?
Option-A) Atlantic Ocean         Option-B) Indian Ocean
Option-C) Pacific Ocean         Option-D) Arctic Ocean
Enter ans (A-D): 
=> c
Checking your answer...
Correct! 🎉

Loading next question...

************************************************************
Question for Rs.3000

(to quit type 'quit' and you will retain the money you won)
3.) Stark Industries is associated with which fictional superhero?
Option-A) Iron Fist         Option-B) Iron Man
Option-C) Hulk         Option-D) Captain America
Enter ans (A-D): 
=> b
Checking your answer...
Correct! 🎉

Loading next question...

************************************************************
Question for Rs.5000

(to quit type 'quit' and you will retain the money you won)
4.) What is the capital of India?
Option-A) Agra         Option-B) New Delhi
Option-C) Delhi         Option-D) Mumbai
Enter ans (A-D): 
=> quit
You chose to Quit!
You leave with Rs.3,000

============================================================
🎉 The Money You Have Won Is => Rs.3,000
Thank you for playing Kaun Banega Crorepati!
---

## Technologies Used 🧰
- **Python 3.12**: The programming language used to create the Kaun Banega Crorepati quiz game.
- **Match-case Statement**: Used for user input handling (available from Python 3.10).
- **Random Module**: Used to shuffle question order each game.
- **Time Module**: Adds realistic delays to enhance gameplay.
```

---

## License 📜
This project is licensed under the MIT License - see the [LICENSE](./LICENSE.txt) file for details.

---

## Author 🙋‍♂️
- **Name**: [Naman Jain](https://github.com/Naman-Jain-2256)
- **Email**: [jain.naman.22560@gmail.com](mailto:jain.naman.22560@gmail.com)