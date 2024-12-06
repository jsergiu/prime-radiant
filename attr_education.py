from random import random
from .person import Person
from .enums import EducationLevel


def calculate_primary_education_probability(age, residence, gender):
    """Calculate probability of having primary education."""
    base_probability = 0.5 if residence == "rural" else 0.3
    if age < 18:
        return 1.0  # Children still in school
    elif age < 25:
        return base_probability * 0.6
    elif age < 40:
        return base_probability * 0.4
    else:
        return base_probability


def calculate_secondary_education_probability(age, residence, gender):
    """Calculate probability of having secondary education."""
    base_probability = 0.4 if residence == "rural" else 0.5
    if age < 18:
        return 0.0  # Too young for high school
    elif age < 25:
        return base_probability * 0.7
    elif age < 40:
        return base_probability * 0.5
    else:
        return base_probability * 0.3


def calculate_undergraduate_probability(age, residence, gender):
    """Calculate probability of having an undergraduate degree."""
    base_probability = 0.1 if residence == "rural" else 0.2
    if gender == "female":
        base_probability += 0.05  # Women have slightly higher rates
    if age < 18:
        return 0.0  # Too young
    elif age < 25:
        return base_probability * 0.6
    elif age < 40:
        return base_probability
    else:
        return base_probability * 0.5


def calculate_postgraduate_probability(age, residence, gender):
    """Calculate probability of having postgraduate education."""
    base_probability = 0.02 if residence == "rural" else 0.08
    if gender == "female":
        base_probability += 0.02  # Women have slightly higher rates
    if age < 25:
        return 0.0  # Too young
    elif age < 40:
        return base_probability * 0.8
    else:
        return base_probability


def assign_education(person: Person):
    """Assign education level to a person."""
    p_primary = calculate_primary_education_probability(person.age, person.residence, person.gender)
    p_secondary = calculate_secondary_education_probability(person.age, person.residence, person.gender)
    p_undergraduate = calculate_undergraduate_probability(person.age, person.residence, person.gender)
    p_postgraduate = calculate_postgraduate_probability(person.age, person.residence, person.gender)

    # Normalize probabilities to ensure they sum to 1
    total = p_primary + p_secondary + p_undergraduate + p_postgraduate
    p_primary /= total
    p_secondary /= total
    p_undergraduate /= total
    p_postgraduate /= total

    # Generate a random number and assign education level
    r = random()
    if r < p_primary:
        person.education = EducationLevel.PRIMARY
    elif r < p_primary + p_secondary:
        person.education = EducationLevel.SECONDARY
    elif r < p_primary + p_secondary + p_undergraduate:
        person.education = EducationLevel.UNDERGRADUATE
    else:
        person.education = EducationLevel.POSTGRADUATE
