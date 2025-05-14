import random
import time

def get_user_pick():
    while True:
        user_pick = input('Pick your choice(rock,paper,scissors):\n=> ').strip().lower()
        if user_pick in game_elements:
            break
        print('Invalid pick! Please pick between rock, paper and scissors.')
    return user_pick

def determine_winner(user_point, computer_point):
    if user_point > computer_point:
        print('Congratulations')
        time.sleep(1)
        print(f'The Player wins with a score of {user_point}-{computer_point} .')
    elif user_point == computer_point:
        print("It's a Draw")
        time.sleep(1)
        print(f"Both Player and Computer has {user_point}")
    else:
        print('Oh no!!!')
        time.sleep(1)
        print(f"Player loses with a score of {user_point}-{computer_point}")
    
def point_distribution(user_pick, computer_pick):
    if user_pick == computer_pick:
            print(f'Both Player and Computer has picked {user_pick}')
            time.sleep(1)
            print("both Computer and Player gets 1 point.")
            return 1,1
    elif (user_pick == 'paper' and computer_pick == 'rock') or \
         (user_pick == 'rock' and computer_pick == 'scissors') or \
         (user_pick == 'scissors' and computer_pick == 'paper'):
        print(f"Player's {user_pick} beats Computer's {computer_pick}")
        time.sleep(1)
        print("Player gets 1 point.")
        return 1,0
    else:
        print(f"Computer's {user_pick} beats Player's {computer_pick}")
        time.sleep(1)
        print("Computer gets 1 point.")
        return 0,1



print(' ROCK PAPER SCISSORS GAME'.center(50, '*'))
print('-'*50 + '\n')

time.sleep(1)
game_elements = ('rock','paper','scissors')
print('''
Rules:
1. Best of 3 rounds.
2. Choices: Rock, Paper, Scissors.
3. Scoring:
   - Rock crushes Scissors
   - Paper covers Rock
   - Scissors cuts Paper
   - Same choice gives both players 1 point
''')

time.sleep(1)
while True:
    game_length = 3
    user_point = 0
    computer_point = 0
    time.sleep(3)
    print('Game Starts in ')
    for i in range(5,0,-1):
        time.sleep(1)
        print(i)
    for i in range(0,game_length):
        computer_pick = random.choice(game_elements)
        user_pick = get_user_pick()
        time.sleep(1.5)
        player_score,computer_score = point_distribution(user_pick, computer_pick)
        user_point += player_score
        computer_point += computer_score
        print('\n' + '-'*50 + '\n')
        time.sleep(1.5)
    time.sleep(2)
    determine_winner(user_point, computer_point)

    while True:
        cont = input('Would like to play again? (y/n):\n=> ').strip().lower()
        if cont in ['y','n']:
            break
        print("Invalid input! Please enter either 'y' or 'n'.")
    if cont == 'n':
        print('\nThank you for playing! 👋\n')
        break
    