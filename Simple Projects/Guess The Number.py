import random
random_num = random.randint(1, 100)

while True:
    user_input = input("Enter a number or 'Quit: ").lower()
    if user_input == 'quit':
        break

    user_input = int(user_input)
    if(user_input == random_num):
        print(f"Success Your {user_input} is the correct number.")
        break
    elif(user_input < random_num):
        print(f"Sorry {user_input} is less then correct number.")
    elif(user_input > random_num):
        print(f"Sorry {user_input} is greater than correct number.")
    else:
        print(f"Sorry {user_input} is not a valid number or too big.")

