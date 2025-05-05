# 🔐 Secret Code Language

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

A fun and beginner-friendly CLI Python tool to **encode** and **decode** words using a custom "secret" format. Designed for practicing string manipulation, conditionals, and user input handling.

---

## 🧠 How It Works

### Encoding Logic

- Takes a user input word.
- Moves the **first character** to the **end** of the word.
- Wraps the result with `LKJ` in the front and `FDS` at the end.

**Example**  
Input: `Hello`  
Process: `elloH` → `LKJelloHFDS`  
Output: `LKJelloHFDS`

---

### Decoding Logic

- Accepts a word in the format `LKJ...FDS`.
- Removes `LKJ` and `FDS`.
- Moves the **last character** to the **front** of the word.

**Example**  
Input: `LKJelloHFDS`  
Process: `elloH` → `Hello`  
Output: `Hello`

> ⚠️ **Note**: The encoding and decoding are **case-sensitive**. `"Hello"` and `"hello"` will be treated as different words.

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

what do you want me to do (encode/decode)?
=> encode
Oh you wish to encode...Okay!

Enter the word to encode(case sensitive):
=> Hello

**************************************************

Your encoded word is: LKJelloHFDS

**************************************************

Would you like to encode or decode another word? (yes/no): no

Thanks for using Secret Code Language! 👋
```

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE.txt) file for details.

---

## 👨‍💻 Author
- **Name**: [Naman Jain](https://github.com/Naman-Jain-2256)
- **Email**: [jain.naman.22560@gmail.com](mailto:jain.naman.22560@gmail.com)

