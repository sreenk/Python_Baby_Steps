###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
ran = digits[:3]
print(ran)
# Another hint:

while(True):
    guess = int(input("What is your guess? "))
    print(guess)

    guess_num = []

    while(guess > 0):
        r = guess % 10
        guess_num.append(r)
        guess = guess//10
    guess_num.reverse()

    check = close =  0

    for i in range(3):
        if guess_num[i] == ran[i]:
            check = check + 1
        elif guess_num[i] in ran:
            close = 1
        else:
            pass

    if check == 3:
        print("Match")
        break
    elif close:
        print("Close")
    else:
        print("No match")




# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
