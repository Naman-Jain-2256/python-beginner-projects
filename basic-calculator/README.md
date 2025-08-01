# 🧮 Basic Calculator

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Status](https://img.shields.io/badge/Status-Improving-blue.svg)

A powerful Python calculator that performs basic and advanced mathematical operations such as addition, subtraction, multiplication, division, square root, exponentiation, logarithms, factorials, and more. It includes input validation and error handling.

---

## ✨ Features

- ➕ Addition (`+`)
- ➖ Subtraction (`-`)
- ✖️ Multiplication (`*`)
- ➗ Division (`/`)
- 🧮 Exponentiation (`exp`)
- ❗ Factorial (`!`) – for non-negative integers only
- 🔢 Modulus (`%`)
- 🔣 Integer Division (`//`)
- 🟰 Percentage (`perc`)
- 📉 Square Root (`sqrt`)
- 🔟 Log Base 10 (`log10`)
- ℯ Natural Log (`ln`)
- 🧠 Input validation (handles invalid numbers, division by zero, and invalid operations)
- 📟 Clean and formatted output

---

## 🛠️ How To Run

1. Install Python 3.10+ (python 3.12 recommended).
2. Clone this repository or download the .py file:
3. navigate to the project directory and run
   ```bash
   python calculator.py
   ```
---

## 🧾 Sample Usage

```bash
     ***************CALCULATOR***************     

==================================================

Enter operator from the list below:
+       : Addition
-       : Subtraction
*       : Multiplication
/       : Division
exp     : Exponentiation (a^b)
!       : Factorial (only for non-negative integers)
perc    : What % is a of b
sqrt    : Square root
log10   : Log base 10
ln      : Natural log (base e)
%       : Modulus (remainder)
//      : Integer division (integer part after division)

"Type 'exit' to quit"


=> +

Enter first number: 10

Enter second number: 5

--------------------------------------------------
The Answer is =  15.0
--------------------------------------------------

do you want to perform another calculation? (y/n): n

Thank You for using CALCULATOR!
```
   
---

## 💻 Sample Code Snippet

```python
def sqrt(n):
    if n < 0:
        print('Value cannot be negative.')
        return None
    return math.sqrt(n)

def factorial(n):
    if n < 0 or not n.is_integer():
        print("Factorials are only defined for positive integers and 0.")
        return None
    return math.factorial(n)

def calculator():
    '''
    A versatile calculator that performs basic and advanced operations.

    Supported Operations:
    +, -, *, /, exp, !, %, sqrt, log10, ln, perc, //
    '''
    # interactive logic here
```

---

## 🧰 Technologies Used

- **Python 3.12**
- **match-case statements** – for operation selection
- **Math module** – for math functions like sqrt, log, factorial
- **CLI interaction** – using input() for user prompts
- **Error handling & validation** – checks for invalid inputs, zero division, etc.

---

## 🚫 Error Handling

- 🚫 Division by zero
- 🚫 Invalid numeric input
- 🚫 Invalid operations
- 🚫 Negative input for `sqrt`, `log10`, `ln`
- 🚫 Non-integers for factorial

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE.txt) file for details.

---

## 🙋‍♂️ Author

- **Name**: [Naman Jain](https://github.com/Naman-Jain-2256)
- **Email**: [jain.naman.22560@gmail.com](mailto:jain.naman.22560@gmail.com)

---

> 🌟 If you find this project helpful, please give it a star!
> Contributions, suggestions, and feedback are welcome.

