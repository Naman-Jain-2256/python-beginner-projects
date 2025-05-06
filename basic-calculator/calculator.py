import math as mt

def sqrt(n):
    if n < 0:
        print('Value cannot be negative.')
        return None
    return mt.sqrt(n)

def log10(n):
    if n <= 0:
        print('Value cannot be negative or 0.')
        return None
    return mt.log10(n)

def ln(n):
    if n <= 0:
        print('Value cannot be negative or 0.')
        return None
    return mt.log(n)

def factorial(n):
    if n<0 or not n.is_integer():
        print("Factorials are only defined for positive integer and 0.")
        return None
    return mt.factorial(n)  

def print_answer(answer):
    '''Prints the result in the desired format'''
    a = "The Answer is = "
    print('\n' + '-'*50 )
    print(a, answer)
    print('-'*50 + '\n')

def calculator():
    '''
    A versatile and interactive CLI calculator for performing basic and advanced mathematical operations.

    ----------------------------------------------------------------
    Supported Operations:
        +       : Addition (a + b)
        -       : Subtraction (a - b)
        *       : Multiplication (a × b)
        /       : Division (a ÷ b)
        //      : Integer Division (quotient without remainder)
        %       : Modulus (remainder of a ÷ b)
        exp     : Exponentiation (a^b)
        !       : Factorial (only for non-negative integers)
        sqrt    : Square Root of a number
        log10   : Logarithm base 10
        ln      : Natural Logarithm (base e)
        perc    : Percentage (What percent is a of b)
    
    ----------------------------------------------------------------
    Usage Instructions:
    1. Choose an operator from the supported list.
    2. Enter the first number.
       - For unary operations (sqrt, log10, ln, !), only one number is required.
       - For binary operations (+, -, *, /, %, exp, perc, //), a second number will be prompted.
    3. Division by zero is not allowed and will prompt re-entry.
    4. Results are displayed in a clean, formatted manner.
    5. Type 'exit' when prompted for an operator to quit the calculator.

    Example:
        Operator: +
        First number: 10
        Second number: 5
        Result: The Answer is = 15.0
    '''
    
    print("***************CALCULATOR***************".center(50))

    valid_operators = ["+", "-", '*', '/', 'exp', '!', '%', 'sqrt', 'log10', 'ln', 'perc', '//']

    while True:
        print('\n' + '='*50)
        print("""
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
        """)
        operator = input("\n=> ").strip().lower()

        if operator == 'exit':
            print('\nThank you for using calculator.')
            break

        if operator not in valid_operators:
            print('INVALID OPERATION')
            continue



        try:
            first = float(input("\nEnter first number: "))
        except ValueError:
            print('\nInvalid input! Please enter a valid number.')
            continue

        if operator not in ['!','log10','ln','sqrt']:

            try:
                second = float(input("\nEnter second number: "))
            except ValueError:
                print('\nInvalid input! Please enter a valid number.')
                continue

            if operator in ['/','%','perc','//']:
                while second == 0:
                    print("\nERROR! division by Zero is not allowed.")
                    try:
                        second = float(input("\nPlease enter a non-zero second number: "))
                    except ValueError:
                        print('\nInvalid input! Please enter a valid number.')
                        continue   

        match operator:
            case "+":
                answer = (first + second)
            case "-":
                answer = (first - second)
            case "*":
                answer = (first*second)
            case "/":
                answer = (first/second)
            case "!":
                try:
                    answer = factorial(first)
                except Exception as e:
                    print(f'Math error: {e}')
                    answer = None
            case "exp":
                answer = (first**second)
            case "log10":
                answer = log10(first)
            case "ln":
                answer = ln(first)
            case 'sqrt':
                answer = sqrt(first)
            case '//':
                answer = (first//second)
            case '%':
                answer = (first%second)
            case 'perc':
                percentage = (first / second) * 100
                answer = f'{percentage:.2f} % of {str(second)}'

            
        if answer is not None:
           print_answer(answer)

        cont=input('do you want to perform another calculation? (y/n): ').strip().lower()
        if cont != "y":
            print('\nThank You for using CALCULATOR!')
            break 

calculator()
