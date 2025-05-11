import random
import string
import time
import re




def random_password_generator():

    def include_type(name):
        while True:
            choice = input(f'Include {name} letters? (y/n): ').lower()
            if choice not in ['y','n']:
                print("Invalid input! Please enter either 'y' or 'n'")
                continue
            return choice == "y"
                 
    def numbers():
        while True:
            numbers = input('Include numbers? (y/n): ').lower()
            if numbers not in ['y','n']:
                print("Invalid input! Please enter either 'y' or 'n'")
                continue
            return numbers == 'y'

    def symbols():
        while True:
            symbols = input('Include symbols? (y/n): ').lower()
            if symbols not in ['y','n']:
                print("Invalid input! Please enter either 'y' or 'n'")
                continue
            return symbols == 'y'

    letters_for_password = ""

    while True:  
        try:
            password_length = int(input('Enter length of password to generate(greater than 4):\n=> '))
            if password_length < 4:
                print("Invalid input! Please enter value greater than or equal to 4 for good password.")
                continue
            break
        except:
            print('Invalid input! Please enter only positive integer.')
            continue
                
    if include_type('uppercase'):
        letters_for_password += string.ascii_uppercase        
            
    if include_type('lowercase'):
        letters_for_password += string.ascii_lowercase        
                
    if numbers():
        letters_for_password += string.digits

    if symbols():
        letters_for_password += string.punctuation

    if not letters_for_password:
        print("❌ You must select at least one character type!")
        return

    generated_password = ''.join(random.choices(letters_for_password,k=password_length))
    print(f"\n✅ Generated Password: {generated_password}\n")
            

def strength_checker():
    def len_check(password):
        if (4 <= len(password) < 6):
            return 1
        elif (6 <= len(password) < 8):
            return 2
        elif len(password) >= 8:
            return 3
        
    input_password = input('Enter the password to check strength:\n=> ').strip()

    uppercase_criteria = re.search(r'[A-Z]', input_password)
    lowercase_criteria = re.search(r'[a-z]', input_password)
    digits_criteria = re.search(r'[0-9]', input_password)
    symbol_criteria = re.search(r'[^\w]', input_password)

    score = ( 
        len_check(input_password)
        +int(bool(uppercase_criteria))
        +int(bool(lowercase_criteria))
        +int(bool(digits_criteria))
        +int(bool(symbol_criteria))
        )
    
    if score >= 7:
        print('Strength: 💪 Very Strong')
    elif score >= 5:
        print('Strength: 👍 Strong')
    elif score >= 3:
        print('Strength: ⚠️ Weak')
    else:
        print('Strength: ❌ Very Weak — Change Immediately!')

   
print("********** PASSWORD GENERATOR AND STRENGTH CHECKER **********".center(75))             
print('-'*75 + '\n')

while True:
    operation = input('Generate password(generate) or check strength(check):\n=> ').strip().lower()
    if operation.lower() not in ['generate','check']:
        print('Invalid opreation! Please enter either "generate" or "check".')
        continue
    
    time.sleep(1)
    if operation == 'check':
        print('\nYou wish to Check strength of your password...Okay!\n')
        time.sleep(1)
        strength_checker()
    elif operation == 'generate':
        print('\nYou wish to generate password...Okay!\n')
        time.sleep(1)
        random_password_generator()
    
    time.sleep(1)   
    while True:    
        cont = input("\nDo you want to use password generator and strength checker again? (y/n):\n=> ")
        print('\n')
        if cont in ['y','n']:
            break
        print("Invalid input! Please enter either 'y' or 'n'.")

    if cont == 'n':
        print('\nThank you for using Password Generator And Strength Checker! 👋\n')
        break
