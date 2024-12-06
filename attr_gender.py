import random

from .person import Person

def assign_gender(person: Person):
    # Define gender probabilities
    genders = {
        "male": 0.49,
        "female": 0.51
    }
    
    # Generate a random number to pick a gender
    r = random.random()
    cumulative_probability = 0.0

    for gender, probability in genders.items():
        cumulative_probability += probability
        if r < cumulative_probability:
            person.gender = gender
            return