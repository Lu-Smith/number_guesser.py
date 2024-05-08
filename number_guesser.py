import random

start = -5
stop = 11

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= start:
        print ("Please write the number bigger than " + start + ".")
        quit()


random_number = random.randint(start, stop)

