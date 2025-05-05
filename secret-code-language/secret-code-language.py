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
        print(f'Your {operation} word is: {output}')
        print('\n' + '*'*50 + '\n')

    while True:
        user_choice = input("\nwhat do you want me to do (encode/decode)? \n=> ").strip().lower()
        if user_choice not in ['decode','encode']:
            print("Invalid Input! Please enter either 'encode' or decode.\n ")
            continue

        print(f'Oh you wish to {user_choice}...Okay!\n')
        
        if user_choice == "encode":
            word_to_encoded = input('Enter the word to encode(case sensitive):\n=> ').strip()
            if len(word_to_encoded) < 1:
                print('You must enter at least one character to encode\n')
                continue
            encoded_word = f'LKJ{word_to_encoded[1:] + word_to_encoded[0]}FDS'
            result(encoded_word,"encoded")
        elif user_choice == 'decode':
            word_to_decode = input('Enter the word to decode(case sensitive):\n=> ').strip()
            if not word_to_decode.startswith('LKJ') or not word_to_decode.endswith('FDS') or len(word_to_decode) < 7:
                print("Invalid encoded format! Make sure it's correctly encoded.\n")
                continue
            trimmed = word_to_decode[3:-3]
            decoded_word = trimmed[-1] + trimmed[:-1]
            result(decoded_word,"decoded")

        cont = input('Would you like to encode or decode another word? (yes/no): ').strip().lower()
        if cont != 'yes':
            print("\nThanks for using Secret Code Language! 👋\n")
            break
    
secret_code_language()