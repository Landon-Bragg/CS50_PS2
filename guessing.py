import random

## try asking for a positive integer
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        #if non integer is given reprompt
    except:
        pass

## make a hidden random number n 
random_number = random.randint(1, level)

## if the guess is larger than n return too large
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > random_number:
                print("Too Large!")
            elif guess < random_number:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        pass
