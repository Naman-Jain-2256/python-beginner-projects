# 🔐 Password Generator and Strength Checker

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Status](https://img.shields.io/badge/Status-Improving-blue.svg)

A simple yet powerful Python tool that allows users to:
- ✅ **Generate strong passwords** based on customizable criteria.
- 🔍 **Check the strength** of any given password using character diversity and length.

---

## 🚀 Features

- Generate random passwords with:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols
- Password length customization
- Strength checker with scoring system:
  - Very Weak ❌
  - Weak ⚠️
  - Strong 👍
  - Very Strong 💪
- User-friendly prompts with error handling
- Reusable and efficient code structure

---

## 🧠 How It Works

1. **Choose an action:**
   - `generate`: Generate a password based on your preferences.
   - `check`: Check the strength of any password.

2. **For generation:**
   - Choose character types (uppercase, lowercase, digits, symbols).
   - Enter the desired password length (must be ≥ 4).
   - Receive a random, secure password.

3. **For strength checking:**
   - Input any password.
   - Get a strength score based on length and character variety.

---

## 📦 Requirements

No external libraries required!  
Only built-in Python modules:
- `random`
- `string`
- `re`
- `time`

---

## ▶️ Usage

```bash
python password-generator-and-strength-checker.py
```
Follow on-screen instructions to either generate a password or check its strength.

---

## 📸 Preview

```bash
       ********** PASSWORD GENERATOR AND STRENGTH CHECKER **********       
---------------------------------------------------------------------------

Generate password(generate) or check strength(check):
=> generate

You wish to generate password...Okay!

Enter length of password to generate(greater than 4):
=> 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

✅ Generated Password: %u6(x32^mY-K

Do you want to use password generator and strength checker again? (y/n):
=> n

Thank you for using Password Generator And Strength Checker! 👋
```

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](../LICENSE.txt) file for details.

---

## 👨‍💻 Author
- **Name**: [Naman Jain](https://github.com/Naman-Jain-2256)
- **Email**: [jain.naman.22560@gmail.com](mailto:jain.naman.22560@gmail.com)