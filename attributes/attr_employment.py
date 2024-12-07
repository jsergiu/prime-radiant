from random import random
from .person import Person
from .enums import EmploymentStatus

"""
Employment Status Categories

We define five possible employment statuses:

    Employed (full-time, part-time, or self-employed)
    Unemployed
    Student
    Retired
    Too Young (under 15)
"""

def calculate_too_young_probability(age):
    """Calculate probability of being too young to work."""
    if age < 15:
        return 1.0
    return 0.0


def calculate_student_probability(age, education):
    """Calculate probability of being a student."""
    if age < 15:
        return 0.0
    elif 15 <= age < 25:
        return 0.8  # Most likely a student in this age range
    elif 25 <= age < 30 and education == "Postgraduate":
        return 0.2  # Possible postgraduate student
    else:
        return 0.0


def calculate_employed_probability(age, education, residence, gender):
    """Calculate probability of being employed."""
    if age < 15 or age >= 65:
        return 0.0  # Too young or retired
    base_probability = 0.7  # General employment rate
    if 18 <= age < 25:
        base_probability *= 0.5  # Many in this range are students
    elif 25 <= age < 55:
        base_probability *= 1.0  # Prime working age
    elif 55 <= age < 65:
        base_probability *= 0.7  # Employment drops approaching retirement

    # Adjust for education level
    if education in ["Undergraduate", "Postgraduate"]:
        base_probability += 0.1
    elif education == "Primary":
        base_probability -= 0.2

    # Adjust for residence
    if residence == "rural":
        base_probability -= 0.1

    # Adjust for gender
    if gender == "female":
        base_probability -= 0.05  # Slightly lower employment rates for women

    return max(0.0, base_probability)  # Ensure probability is non-negative


def calculate_unemployed_probability(age, employed_probability, student_probability):
    """Calculate probability of being unemployed."""
    if age < 18 or age >= 65:
        return 0.0  # Too young or retired
    return max(0.0, 1.0 - (employed_probability + student_probability))


def calculate_retired_probability(age):
    """Calculate probability of being retired."""
    if age >= 65:
        return 1.0
    elif 55 <= age < 65:
        return 0.3  # Early retirement possibilities
    else:
        return 0.0


def assign_employment(person: Person):
    """Assign employment status to a person."""
    p_too_young = calculate_too_young_probability(person.age)
    if p_too_young == 1.0:
        person.employment = EmploymentStatus.TOO_YOUNG
        return

    p_student = calculate_student_probability(person.age, person.education)
    p_employed = calculate_employed_probability(person.age, person.education, person.residence, person.gender)
    p_retired = calculate_retired_probability(person.age)
    p_unemployed = calculate_unemployed_probability(person.age, p_employed, p_student)

    # Normalize probabilities to sum to 1
    total = p_student + p_employed + p_unemployed + p_retired
    p_student /= total
    p_employed /= total
    p_unemployed /= total
    p_retired /= total

    # Generate a random number to assign employment status
    r = random()
    if r < p_student:
        person.employment = EmploymentStatus.STUDENT
    elif r < p_student + p_employed:
        person.employment = EmploymentStatus.EMPLOYED
    elif r < p_student + p_employed + p_unemployed:
        person.employment = EmploymentStatus.UNEMPLOYED
    else:
        person.employment = EmploymentStatus.RETIRED
