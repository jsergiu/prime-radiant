from random import random
from .person import Person
from .enums import MaritalStatus


def calculate_never_married_probability(x):
    if x < 18:
        return 1
    elif 18 <= x < 30:
        return 1 - 0.05 * (x - 18)
    elif 30 <= x < 50:
        return 0.1
    else:
        return 0

def calculate_married_probability(x):
    if x < 18:
        return 0
    elif 18 <= x < 30:
        return 0.05 * (x - 18)
    elif 30 <= x < 50:
        return 0.75
    elif 50 <= x < 70:
        return 0.75 - 0.02 * (x - 50)
    else:
        return 0.35

def calculate_widow_probability(x):
    if x < 50:
        return 0
    elif 50 <= x < 70:
        return 0.02 * (x - 50)
    else:
        return 1 - calculate_married_probability(x)
    

def assign_marital_status(person: Person):
    probability_never_married  = calculate_never_married_probability(person.age)
    probability_married  = calculate_married_probability(person.age)
    probability_widow  = calculate_widow_probability(person.age)

    # Generate a random number and assign a status
    r = random()
    
    if r < probability_never_married :
        person.marital_status = MaritalStatus.NEVER_MARRIED
    elif r < probability_never_married + probability_married :
        person.marital_status = MaritalStatus.MARRIED
    else:
        person.marital_status = MaritalStatus.WIDOW

    