import random
import string
import re

def random_password_generator():
    print("********** PASSWORD GENERATOR **********".center(50))
    print('-'*50 + '\n')

    def upper_case():
        while True:
            upper_case = input('Include Uppercase? (y/n): ').lower()
            if upper_case not in ['y','n']:
                print("Invalid input! Please enter either 'y' or 'n'")
                continue
            return upper_case == "y"
            
    def lower_case():
        while True:
            lower_case = input('Include Lowercase? (y/n): ').lower()
            if lower_case not in ['y','n']:
                print("Invalid input! Please enter either 'y' or 'n'")
                continue
            return lower_case == 'y'
                 
    def numbers():
        while True:
            numbers = input('Include Numbers? (y/n): ').lower()
            if numbers not in ['y','n']:
                print("Invalid input! Please enter either 'y' or 'n'")
                continue
            return numbers == 'y'

    def symbols():
        while True:
            symbols = input('Include Symbols? (y/n): ').lower()
            if symbols not in ['y','n']:
                print("Invalid input! Please enter either 'y' or 'n'")
                continue
            return symbols == 'y'
        



    while True:
        operation = input('"Generate password(genp) or check strength(strcheck)":\n=> ').strip()
        if operation.lower() not in ['genp','strcheck']:
            print('Invalid opreation! please enter either "genp" or "strcheck".')
            continue
        
        if operation == 'strcheck':
            print('Okay you wish to ')
            pass
        elif operation == 'genp':
            letters_for_password = ""
            print('\nYou wish to generate password...Okay!')
            
             
            try:
               password_length = int(input('Enter length of password to generate(greater than 4):\n=> '))
               if password_length < 4:
                   print("Invalid input! Please enter value greater than or equal to 4 for good password.")
                   continue
            except:
                print('Invalid input! Please enter only positive integer.')
                continue
                
            upper_letters = upper_case()
            if upper_letters is True:
                letters_for_password += string.ascii_uppercase        
                
            lower_letters = lower_case()
            if lower_letters is True:
                letters_for_password += string.ascii_lowercase        
                
            digits = numbers()
            if digits is True:
                letters_for_password += string.digits

            sym_letters = symbols()
            if sym_letters is True:
                letters_for_password += string.punctuation

            if not letters_for_password:
                print("❌ You must select at least one character type!")
                continue

                
            generated_password = ''.join(random.choices(letters_for_password,k=password_length))
            print(f"\n✅ Generated Password: {generated_password}\n")
            

                
                
                





random_password_generator()