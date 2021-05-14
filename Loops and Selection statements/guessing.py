import pdb
import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
maxattempt = math.ceil(math.log(larger-smaller))
count = 0
guess = int((smaller + larger)/2)

while count != maxattempt:
    count += 1
    guess = int((smaller + larger)/2)
    print(smaller,larger)
    print("Your number is: ",guess)
    hlp = input("Enter =, <, or >: ")
    if hlp == '>':
        smaller = guess+1
    elif hlp == '<':
        larger = guess-1
    elif hlp == '=':
        print("Hooray, I've got it in", count, "tries!")
    else:
        print("I'm out of guesses, and you cheated")
        break