def secret_code_language():
    """
    This is a secret code language function
    which can encode and decode words.

    ---
    HOW TO USE:
    1. Choose whether you want to encode or decode.
       (If you enter anything else, you'll be prompted again.)
    2. If you choose 'encode', enter the word to encode (case sensitive).
       It will be transformed and displayed.
    3. If you choose 'decode', enter the encoded word (case sensitive).
       It will be decoded and displayed.
    """
    print('\n' + '**********SECRET CODE LANGUAGE**********'.center(50))
    print('-'*50)

    def result(output,operation=''):
        print('\n' + '*'*50 + '\n')
        print(f'Your {operation.capitalize()} Message is: {output}')
        print('\n' + '*'*50 + '\n')

    def encrypt():
        while True:
            message_to_encrypt = input("Enter message to encrypt (case-sensitive):\n=> ").strip()
            if len(message_to_encrypt) < 1:
               print('You must enter at least one character.\n')
               continue

            message_words = message_to_encrypt.split(' ')
            encrypted_words_list = []
            for word in message_words:
                if len(word) > 3:
                    word1 = f'LkJ{word[1:]+word[0]}FdS'
                    encrypted_words_list.append(word1)
                else:
                    word2 = word[::-1]
                    encrypted_words_list.append(word2)
            return " ".join(encrypted_words_list)
    
    def decrypt():
        while True:
            message_to_decrypt = input('Enter message to decrypt(case sensitive):\n=> ').strip()
            if len(message_to_decrypt) < 1:
                print('You must enter at least one character.\n')
                continue
            message_words = message_to_decrypt.split(' ')
            decrypted_words_list = []
            for word in message_words:
                if len(word) < 4:
                    word1 = word[::-1]
                    decrypted_words_list.append(word1)
                else:
                    if  word.startswith("LkJ") and word.endswith('FdS') and len(word) >= 7:
                        trimmed = word[3:-3]
                        word2 = trimmed[-1] + trimmed[:-1]
                        decrypted_words_list.append(word2)
                    else:
                        print("Invalid encoded format! Make sure it's correctly encoded.\n")
                        return None
            return ' '.join(decrypted_words_list)     
                    
    while True:
        user_choice = input("\nWhat do you want me to do (encrypt/decrypt)? \n=> ").strip().lower()
        if user_choice not in ['decrypt','encrypt']:
            print("Invalid Input! Please enter either 'encrypt' or 'decrypt'.\n ")
            continue

        print(f'Oh you wish to {user_choice}...Okay!\n')
        
        if user_choice == "encrypt":
            encrypted_message = encrypt()
            result(encrypted_message,user_choice + 'ed')
            
        elif user_choice == 'decrypt':
            decrypted_message = decrypt()
            if decrypted_message is not None:
                result(decrypted_message,user_choice + 'ed')
        
        while True:
            cont = input('Would you like to encrypt or decrypt another message? (y/n): ').strip().lower()
            if cont in ['y','n']:
                break
            print('\nInvalid input! Please enter either "y" or "n".\n')
            
        if cont == 'n':
            print("\nThanks for using Secret Code Language! 👋\n")
            break
    
if __name__ == "__main__":
    secret_code_language()