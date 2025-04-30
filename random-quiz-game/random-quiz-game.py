import random

print("Welcome to the Quiz Game! 🎉 Answer the following questions:".center(140))

CORRECT = 0
questions = [
    "In which city one of the seven wonders of world \"Tajmahal\" is located?", 
    "National bird of India?", 
    "Which animal is known as the \"King of the Jungle\"?", 
    "What is the national animal of India?", 
    "What is the capital city of India?", 
    "Which ocean is the largest in the world?", 
    "What do you call a baby cat?", 
    "How many months are there in a year?", 
    "How many days are there in a week?", 
    "What is the name of the currency of India?"
]

answers = [
    "AGRA",
    "PEACOCK",
    "LION",
    "TIGER",
    "NEW DELHI",
    "PACIFIC OCEAN",
    "KITTEN",
    "12",
    "7",
    "RUPEE"
]

while len(questions) > 0 :
    i = random.choice(questions)
    print(i)
    b = questions.index(i)
    c = answers[b]
    user_input = input("ans =>").strip().upper()
    questions.pop(b)
    answers.pop(b)
    
    if user_input == c:
        CORRECT += 1

    else:
        continue
print(f'Your score is {CORRECT} out of 10')
