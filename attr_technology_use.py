import random

from .person import Person

"""
    Non-User: Individuals not using the internet or social media.
    Basic User: Individuals using the internet for essential tasks (e.g., email, basic browsing).
    Social Media User: Individuals actively engaging on platforms like Facebook, Instagram, and TikTok.
    Advanced User: Individuals utilizing technology extensively, including streaming, online shopping, and content creation.

Key Influencing Factors:

    Age: Younger individuals are more likely to be advanced users, while older individuals may be non-users or basic users.
    Residence: Urban residents typically have higher technology adoption rates than rural residents.
    Income: Higher income levels correlate with increased access to technology and advanced usage.
    Education: Higher education levels are associated with greater technology proficiency.
"""

from random import random
from .person import Person
from .enums import TechnologyUse

def calculate_non_user_probability(age, residence, income, education):
    """Calculate probability of being a non-user."""
    base_probability = 0.1  # General baseline
    if age > 65:
        base_probability += 0.3  # Older individuals less likely to use technology
    if residence == "rural":
        base_probability += 0.1  # Rural areas have lower internet penetration
    if income == "low":
        base_probability += 0.1  # Lower income affects access to technology
    if education == "Primary":
        base_probability += 0.1  # Lower education correlates with less tech use
    return min(1.0, base_probability)

def calculate_basic_user_probability(age, residence, income, education):
    """Calculate probability of being a basic user."""
    base_probability = 0.3  # General baseline
    if age > 50:
        base_probability += 0.2
    if residence == "rural":
        base_probability += 0.1
    if income == "medium":
        base_probability += 0.1
    if education == "Secondary":
        base_probability += 0.1
    return min(1.0, base_probability)

def calculate_social_media_user_probability(age, residence, income, education):
    """Calculate probability of being a social media user."""
    base_probability = 0.4  # General baseline
    if 18 <= age <= 35:
        base_probability += 0.2  # Younger individuals more active on social media
    if residence == "urban":
        base_probability += 0.1
    if income == "medium" or income == "high":
        base_probability += 0.1
    if education in ["Secondary", "Undergraduate"]:
        base_probability += 0.1
    return min(1.0, base_probability)

def calculate_advanced_user_probability(age, residence, income, education):
    """Calculate probability of being an advanced user."""
    base_probability = 0.2  # General baseline
    if 18 <= age <= 45:
        base_probability += 0.2
    if residence == "urban":
        base_probability += 0.1
    if income == "high":
        base_probability += 0.2
    if education in ["Undergraduate", "Postgraduate"]:
        base_probability += 0.2
    return min(1.0, base_probability)

def assign_technology_use(person: Person):
    """Assign technology use category to a person."""
    p_non_user = calculate_non_user_probability(person.age, person.residence, person.income, person.education)
    p_basic_user = calculate_basic_user_probability(person.age, person.residence, person.income, person.education)
    p_social_media_user = calculate_social_media_user_probability(person.age, person.residence, person.income, person.education)
    p_advanced_user = calculate_advanced_user_probability(person.age, person.residence, person.income, person.education)

    # Normalize probabilities to ensure they sum to 1
    total = p_non_user + p_basic_user + p_social_media_user + p_advanced_user
    p_non_user /= total
    p_basic_user /= total
    p_social_media_user /= total
    p_advanced_user /= total

    # Generate a random number to assign technology use category
    r = random()
    if r < p_non_user:
        person.technology_use = TechnologyUse.NON_USER
    elif r < p_non_user + p_basic_user:
        person.technology_use = TechnologyUse.BASIC_USER
    elif r < p_non_user + p_basic_user + p_social_media_user:
        person.technology_use = TechnologyUse.SOCIAL_MEDIA_USER
    else:
        person.technology_use = TechnologyUse.ADVANCED_USER
