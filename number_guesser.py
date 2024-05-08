import random

start = -5
stop = 11

top_of_range = input("Type a number: ")

if top_of_range.lstrip('-').isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= start:
        print ("Please write the number larger than ", start," next time.")
        quit()

else :
    print ("Please write a number next time.")
    quit()

random_number = random.randint(start, top_of_range)
print("Random number between", start, "and", top_of_range)

while True:
    user_guess = input("Make your guess ")

    if user_guess.lstrip('-').isdigit():
        user_guess = int(user_guess)

    else :
        print ("Please write a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("You didn't got it!")



