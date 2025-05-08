import random
import time

def guess_the_number_game():
    while True:

        print('********** GUESS THE NUMBER **********'.center(50))
        print('-'*50 + '\n')
        time.sleep(1)
        print("INSTRUCTIONS:-")
        time.sleep(1)
        print('1. Guess a number in between (1-50)')
        time.sleep(1.5)
        print("2. You have 5 chances to guess the correct number between 1 and 50.")
        time.sleep(1.5)
        print("3. After each guess, you'll be told if the correct number is higher or lower.\n")
    

        LOW = 1
        HIGH = 50
        MAX_ATTEMPTS = 5

        number = random.randint(LOW,HIGH)
        attempts_left = MAX_ATTEMPTS

        while attempts_left > 0:
            time.sleep(1.5)
            print(f'\nYou have {attempts_left} chances left!')

            try:
                user_guess = int(input('Enter your guess :\n=> ').strip())
            except ValueError:
                print('Invalid input! Please enter a valid number.')
                continue
            if not (LOW <= user_guess <= HIGH):
                time.sleep(1)
                print(f'Please enter number between {LOW} and {HIGH}.')
                continue

            attempts_left -= 1
            time.sleep(1)
            print('\nChecking your guess...\n')
            time.sleep(1.5)
            if user_guess > number:
                print(f'❌ No! the number is less than {user_guess}.')
            elif user_guess < number:
                print(f'❌ No! the number is greater than {user_guess}.')
            elif user_guess == number:
                print('Congratulations! 🎉 You guessed it correct.')
                break
        else:
            print('\n😢 Oh ho You exhausted all your chances ')
            print(f'The number was {number}')
            
        play_again = input('\nWould you like to play again? (y/n) => ').strip().lower()
        if play_again != 'y':
            break

    print('\n🎮 Thank you for Playing Guess The Number Game! 👋')

if __name__ == "__main__":
    guess_the_number_game()
