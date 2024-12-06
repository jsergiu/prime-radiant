import random

from .person import Person

def assign_income(person: Person):
    # No income for people under 16 years old
    if person.age < 16:
        person.income = 0
        return
    
    # Base income ranges based on age
    if person.age < 25:
        base_income = random.randint(0, 300)  # Younger people tend to have lower incomes
    elif person.age < 65:
        base_income = random.randint(200, 1000)  # Working-age population has a higher range
    else:
        base_income = random.randint(0, 400)  # Seniors often have lower fixed incomes

    # Apply marital status modifier
    if person.marital_status == "married":
        base_income += random.randint(100, 200)  # Married individuals have higher income on average

    # Add randomness to simulate diverse income distributions
    fluctuation = random.randint(-50, 50)
    person.income = max(0, base_income + fluctuation)  # Ensure income is non-negative
