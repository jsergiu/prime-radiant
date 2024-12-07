
import random
from .person import Person


def assign_age(person: Person):
    # Define age groups and their probabilities
    age_groups = {
        (0, 14): 0.46,
        (15, 24): 0.10,
        (25, 54): 0.16,
        (55, 64): 0.13,
        (65, 99): 0.15
    }
    
    # Generate a random number to pick an age group
    r = random.random()
    cumulative_probability = 0.0

    for age_range, probability in age_groups.items():
        cumulative_probability += probability
        if r < cumulative_probability:
            # Assign a random age within the selected range
            person.age = random.randint(age_range[0], age_range[1])
            return
    
    