# 🔐 Secret Code Language

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

A fun and beginner-friendly CLI Python tool to **encrypt** and **decrypt** words using a custom "secret" format. Designed for practicing string manipulation, conditionals, and user input handling.

---

## 📋 Table of Contents

- [🔐 Secret Code Language](#-secret-code-language)
- [🧠 How It Works](#-how-it-works)
  - [Encryption Logic](#encryption-logic)
  - [Decryption Logic](#decryption-logic)
- [💻 How to Run](#-how-to-run)
- [🧪 Sample Output](#-sample-output)
- [📜 License](#-license)
- [👨‍💻 Author](#-author)

---

## 🧠 How It Works

### Encryption Logic

- Takes a user input message.
- For each word in the message:
  - If the word has more than 3 characters, moves the **first character** to the **end** of that word.
  - If the word has 3 characters or fewer, it is reversed instead.
- Wraps **each word** with `LkJ` in the front and `FdS` at the end.

**Example**  
Input: `Hello`  
Process: `elloH` → `LkJelloHFdS`  
Output: `LkJelloHFdS`

---

### Decryption Logic

- Accepts a message where each word is in the format `LkJ...FdS`.
- Removes `LkJ` and `FdS`.
- For each word in the message:
  - If the word has more than 3 characters, moves the **last character** to the **front** of that word.
  - If the word has 3 characters or fewer, it is reversed back to the original.

**Example**  
Input: `LkJelloHFdS`  
Process: remove wrapper → `elloH` → move last letter to front → `Hello`  
Output: `Hello`

> ⚠️ **Note**: The encryption and decryption are **case-sensitive**. `"Hello"` and `"hello"` will be treated as different words.

---

## 💻 How to Run

1. Make sure Python 3 is installed.
2. Save the script as `secret_code_language.py`.
3. Run the script in your terminal:

```bash
python secret-code-language.py
```

---

## 🧪 Sample Output
```bash
     **********SECRET CODE LANGUAGE**********
--------------------------------------------------

What do you want me to do (encrypt/decrypt)?
=> encrypt
Oh you wish to encrypt...Okay!

Enter message to encrypt (case-sensitive):
=> hello world

**************************************************

Your Encrypted Message is: LkJellohFdS LkJorldwFdS

**************************************************

Would you like to encrypt or decrypt another message? (y/n): n

Thanks for using Secret Code Language! 👋
```
> ℹ️ Note: Each word in the message is encrypted or decrypted individually with its own wrapper.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE.txt) file for details.

---

## 👨‍💻 Author
- **Name**: [Naman Jain](https://github.com/Naman-Jain-2256)
- **Email**: [jain.naman.22560@gmail.com](mailto:jain.naman.22560@gmail.com)