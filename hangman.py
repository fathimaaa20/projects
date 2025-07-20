import random

def hangman():
    words=["Python","java","ruby","kotlin","swift","javascript","typescript","csharp","golang","rust","dart"]
    word=random.choice(words).upper()
    word_display=["_" for _ in word] # create a list of underscores for each letter in the word
    attempts=6

    print("Welcome to Hangman!")

    while attempts > 0 and "_" in word_display:
        




