import random

def guess(x):#user guesses a number between 1 and x and computer gives feedback
    
    random_number=random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess=int(input(f"Guess a number between 1 and {x}"))
        if guess <random_number:
            print("Sorry, guess a higher value.")
        elif guess > random_number:
            print("Sorry, guess a lower value.")
    print(f"Congratulations! You have guessed the number {random_number} correctly.")



def computer_guess(x):#computer guesses a number between 1 and x and user gives feedback
    low = 1
    high = x
    feedback = ''
    while feedback!='c' and low!= high :
        guess = random.randint(low, high)
        feedback=input(f"Is {guess} too high (H),too low (L), or correct (C)? ").lower()
        if feedback=='h':
            high =guess-1
        if feedback=='l':
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess}, correctly!") 

computer_guess(10)           