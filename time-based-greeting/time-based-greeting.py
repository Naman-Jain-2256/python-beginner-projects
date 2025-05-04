import time

# Get the current time in HH:MM:SS format
timestamp = time.strftime('%H:%M:%S')

# Ask for user's name
T = input("Your Name Is? \n")

# Greet based on the time of day
if "06:00:00" <= timestamp <= "11:59:59":
    print("Good Morning", T)
elif "12:00:00" <= timestamp <= "17:59:59":
    print("Good Afternoon", T)
elif "18:00:00" <= timestamp <= "21:59:59":
    print("Good Evening", T)
else:
    print("Good Night", T)

# Print each character of the current time
for character in timestamp:
    print(character, end="")
