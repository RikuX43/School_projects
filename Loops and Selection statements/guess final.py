# Modify the code below:
import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
attempts_number = math.ceil(math.log2(larger-smaller))
guesses = int((smaller + larger)/2)

count = 0
while count != attempts_number:
    count += 1
    guesses = int((smaller+larger)/2)
    print(smaller,larger)
    print("Your number is", guesses)
    in_put = input("Enter =, <, or >: ")
    if in_put == '>':
        smaller = guesses + 1
    elif in_put == '<':
        larger = guesses - 1
    elif in_put == '=':
        print("Hooray, I've got it in", count, "tries!")
        break
else:
    print("I'm out of guesses and you cheated")
    
