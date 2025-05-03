import time



def options(a):
    match a:
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
            return 3
        case 'D':
            return 4
        case 'QUIT':
            return 'quit'
   
print("********** WELCOME TO KAUN BANEGA CROREPATI **********\n")
time.sleep(1.5)

questions = [
    ["How many continents are there in the world?", "7", '6', '9', '8', 1],
    ['What is the capital of India?', 'Agra', 'New Delhi', 'Delhi', 'Mumbai', 2],
    ['Which is the largest ocean in the world?', 'Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean', 'Arctic Ocean', 3],
    ['India is a part of which continent?', 'Asia', 'Africa', 'Antarctica', 'North America', 1],
    ['Which planet is called a red planet?', 'Jupiter', 'Mercury', 'Uranus', 'Mars', 4],
    ['Lemons and oranges are rich in which vitamin?', 'Vitamin C', "Vitamin K", 'Vitamin A', 'Vitamin D', 1],
    ['What is the formula of common salt?', 'NaCl', "KCl", 'LiCl', 'CaCl2', 1],
    ['Which planet is the Largest planet in the solar system?', 'Jupiter', 'Neptune', 'Earth', 'Mercury', 1],
    ['What is celebrated on 15th August?', 'Independence Day', 'Gandhi Jayanti', 'Republic Day', 'Christmas Day', 1],
    ['Stark Industries is associated with which fictional superhero?', 'Iron Fist', 'Iron Man', 'Hulk', 'Captain America', 2]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
SAFE_LEVEL = 10000


money = 0

for i in range(len(questions)):
    question = questions[i]
    print("\n" + "*"*60)
    print(f'Question for Rs.{levels[i]}\n \n(to quit type \'quit\' and you will retain the money you won)')
    print(f'{i+1}.)', question[0])
    print(f'Option-A) {question[1]}         Option-B) {question[2]}\nOption-C) {question[3]}         Option-D) {question[4]}')
    time.sleep(0.5)
    user_input = input("Enter ans (A-D): \n=> ").strip().upper()
    ans = options(user_input)
    
    if ans == question[5]:
        money = levels[i]
        print('Checking your answer...')
        time.sleep(2)
        print("Correct! 🎉\n")
        time.sleep(1.5)
    elif ans == 'quit':
        print('You chose to Quit!')
        break
    else:
        print('Wrong Answer!!!!!\nYou Lost ❌')
        correct_answer = ['A', 'B', 'C', 'D']
        time.sleep(1.5)
        print(f'The Correct was : Option-{correct_answer[question[5]-1]}) {question[question[5]]}')
        print(f'You leave with Rs.{money}')
        if i >= 5:
            money = SAFE_LEVEL
        else :
            money = 0
        break

time.sleep(1.5)
print("\n" + "="*60)
print(f"🎉 The Money You Have Won Is => Rs.{money}")
print("Thank you for playing Kaun Banega Crorepati!\n")