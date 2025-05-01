# Basic Calculator 🧮

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Status](https://img.shields.io/badge/Status-In%20Progress-brightyellow.svg)

A simple Python calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, division, and also handles advanced operations such as factorial and exponentiation. It includes error handling for division by zero and input validation for the factorial operation.

## Features ✨
- Addition (+)
- Subtraction (-)
- Multiplication (x)
- Division (/) (with division by zero check)
- Factorial (!) for non-negative integers
- Exponentiation (exp) for powers

## How to Run 🛠️
1. Install Python 3 (if not already installed).
2. Clone this repository or download the .py file:
3. navigate to the project directory and run
   ```bash
   python calculator.py
   
## Code Example 💻
```python
def factorial(n):
    if n==0 or n==1 :
        return 1 
    elif n<0 or not n.is_integer() :
        print("Factorials are only defined for positive integer and 0")
        return None
    else:
        return n*factorial(n-1)  

def print_answer(answer):
    '''Prints the result in the desired format'''
    a = "The Answer is = "
    print('\n' + '-'*50 )
    print(a, answer)
    print('-'*50 + '\n')

def calculator():
    '''It is a simple calculator that does basic arithmetic operations:
       addition(+), subtraction(-), division(/), multiplication(x)
       and two more advanced operations: factorial(!), and exponent(exp) 
     
     ---
     HOW TO USE :-
     1. Enter the operator you want to use(+,-,/,x,!,exp).
        (Enter from above mentioned operator only else it will say 'INVALID OPERATION') 
     2. Enter the first number.
        (For '!', enter a positive integer only, or you will get a warning.)
     3. If operator is not '!', you will be asked for a second number.
        (do not enter 0 if the operator is '/', else you will be asked again).
     4. The result will be displayed.
     
     
     '''
    print("***************CALCULATOR***************".center(100))

    valid_operators = ["+", "-", 'x', '/', 'exp', '!']

    while True:
        operator = input("Enter operator [+,-,x,/,!(factorial),exp(exponent)]: ").strip()

        if operator not in valid_operators:
            print('INVALID OPERATION')
            continue

        first = float(input("Enter first number: "))

        if operator not in ['!']:

            if operator == '/':
                second = float(input("Enter second number (non-zero): "))
                while second == 0:
                    print("ERROR! division by Zero is not allowed.")
                    second = float(input("Please enter a non-zero second number: "))
            else :   
                second = float(input("Enter second number: "))     

        match operator:
            case "+":
                answer = (first + second)
            case "-":
                answer = (first - second)
            case "x":
                answer = (first*second)
            case "/":
                answer = (first/second)
            case "!":
                answer = factorial(first)
            case "exp":
                answer = (first**second)
            
        if answer is not None:
           print_answer(answer)

        cont=input('do you want to perform another calculation? (yes/no): ').strip().lower()
        if cont != "yes":
            break 

calculator()

```
## Technologies Used 🧰
- **Python 3.12**: The programming language used to create the calculator.
- **Match-case Statement**: Used for handling arithmetic operations in Python (available from Python 3.10).
- **Recursion**: Used for calculating factorials

## License 📜
This project is licensed under the MIT License - see the [LICENSE](./LICENSE.txt) file for details.

## Author 🙋‍♂️
- **Name**: [Naman Jain](https://github.com/Naman-Jain-2256)
- **Email**: [jain.naman.22560@gmail.com](mailto:jain.naman.22560@gmail.com)





