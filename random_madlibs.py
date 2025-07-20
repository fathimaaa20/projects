import random

# Word lists
names = ["Fathima", "Hashna", "Aisha", "Hafsa", "Haniya", "Nadiya", "Sana"]
adjectives = ["brave", "beautiful", "happy", "excited", "curious", "funny", "silly"]
verb1 = ["dance", "sing", "play", "run", "code", "explore"]
verb2 = ["jump", "swim", "climb", "write", "draw", "cook"]
places = ["forest", "beach", "mountain", "city", "desert", "park"]
objects = ["magic wand", "treasure chest", "ancient book", "mysterious key", "glowing crystal"]
adverbs = ["quickly", "silently", "happily", "sadly", "excitedly", "curiously"]
creatures = ["unicorn", "dragon", "fairy", "elf", "goblin", "mermaid"]

# Function to generate story
def generate_randommadlib():
    name = random.choice(names)
    adj = random.choice(adjectives)
    v1 = random.choice(verb1)
    v2 = random.choice(verb2)
    place = random.choice(places)
    object1 = random.choice(objects)
    adverb = random.choice(adverbs)
    creature = random.choice(creatures)

    story = f"""
    🌟 Once upon a time, there lived a {adj} girl named {name}.
    She loved to {v1} every day and would always {adverb} {v2} in the {place}.
    One day, she discovered a {object1} and met a magical {creature}. 🧚‍♀️
    They became friends and had many amazing adventures together! 🌈
    """
    return story

# Main block
if __name__ == "__main__":
    print(generate_randommadlib())
