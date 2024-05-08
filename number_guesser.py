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
print("Random number between", start, "and", top_of_range, ":", random_number)

