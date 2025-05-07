import time
import random



def options(a):
    a = a.upper()
    match a:
        case 'A':
            return 0
        case 'B':
            return 1
        case 'C':
            return 2
        case 'D':
            return 3
        case 'QUIT':
            return 'quit'
        case _:
            print('Invalid input! Please enter a value from(A,B,C,D):')
            return None
   
print("********** WELCOME TO KAUN BANEGA CROREPATI **********\n".center(60))
time.sleep(1.5)

questions = [
    ["How many continents are there in the world?", ["7", '6', '9', '8'], 0],
    ['What is the capital of India?', ['Agra', 'New Delhi', 'Delhi', 'Mumbai'], 1],
    ['Which is the largest ocean in the world?', ['Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean', 'Arctic Ocean'], 2],
    ['India is a part of which continent?', ['Asia', 'Africa', 'Antarctica', 'North America'], 0],
    ['Which planet is called a red planet?', ['Jupiter', 'Mercury', 'Uranus', 'Mars'], 3],
    ['Lemons and oranges are rich in which vitamin?', ['Vitamin C', "Vitamin K", 'Vitamin A', 'Vitamin D'], 0],
    ['What is the formula of common salt?', ['NaCl', "KCl", 'LiCl', 'CaCl2'], 0],
    ['Which planet is the Largest planet in the solar system?', ['Jupiter', 'Neptune', 'Earth', 'Mercury'], 0],
    ['What is celebrated on 15th August?', ['Independence Day', 'Gandhi Jayanti', 'Republic Day', 'Christmas Day'], 0],
    ['Stark Industries is associated with which fictional superhero?', ['Iron Fist', 'Iron Man', 'Hulk', 'Captain America'], 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
SAFE_LEVEL = 10000


money = 0

random.shuffle(questions)
for i in range(len(questions)):
    
    if i > 0:
        print('Loading next question...')
        time.sleep(1)

    question = questions[i]
    print("\n" + "*"*60)
    print(f'Question for Rs.{levels[i]}\n \n(to quit type \'quit\' and you will retain the money you won)')
    print(f'{i+1}.)', question[0])
    print(f'Option-A) {question[1][0]}         Option-B) {question[1][1]}\nOption-C) {question[1][2]}         Option-D) {question[1][3]}')
    time.sleep(0.5)
        
    while True:
        user_input = input("Enter ans (A-D): \n=> ").strip()
        ans = options(user_input)
    
        if ans != None:
            break

    if ans == question[2]:
        money = levels[i]
        print('Checking your answer...')
        time.sleep(2)
        print("Correct! 🎉\n")
        time.sleep(1.5)
    elif ans == 'quit':
        print('You chose to Quit!')
        print(f'You leave with Rs.{money:,}')
        break
    else:
        print('Wrong Answer!!!!!\nYou Lost ❌')
        correct_answer = ['A', 'B', 'C', 'D']
        time.sleep(1.5)
        print(f'The Correct was : Option-{correct_answer[question[2]]}) {question[1][question[2]]}')
        if i >= 5:
            money = SAFE_LEVEL
        else :
            money = 0
        print(f'You leave with Rs.{money:,}')
        break
else:
    print("\n🎉 Congratulations! You have answered all questions correctly and won the grand prize of Rs.320,000!")
    time.sleep(1.5)

time.sleep(1.5)
print("\n" + "="*60)
print(f"🎉 The Money You Have Won Is => Rs.{money:,}")
print("Thank you for playing Kaun Banega Crorepati!\n")