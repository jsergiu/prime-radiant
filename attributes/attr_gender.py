import random

from .person import Person
from .enums import Gender

def assign_gender(person: Person, gender_ratio: float):
    # Define gender probabilities
    genders = {
        Gender.MALE: gender_ratio,
        Gender.FEMALE: 1 - gender_ratio
    }
    
    # Generate a random number to pick a gender
    r = random.random()
    cumulative_probability = 0.0

    for gender, probability in genders.items():
        cumulative_probability += probability
        if r < cumulative_probability:
            person.gender = gender
            return