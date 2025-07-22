import random
words=["Java","Python","Javascript","Ruby","C++","C#","Swift","Go","Kotlin","PHP"]
choose_word=random.choice(words)
choose_word=["_" for _ in choose_word]#create a list of underscore
attempts=8
print("Welcome to the Hangman game!")

