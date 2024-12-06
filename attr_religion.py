from random import random
from .person import Person
from .enums import Religion

"""
Major Religions in Romania (Based on Census Data)

Orthodox Christian (~85%)
Roman Catholic (~5%)
Protestant (~3%)
Other (e.g., Greek Catholic, Muslim, Jewish, atheist, agnostic) (~7%)


Key Influencing Factors

Residence:
    Rural areas are predominantly Orthodox.
    Urban areas have more diversity, with higher percentages of Catholics, Protestants, and "Other."

Ethnicity (Optional, if ethnicity is an attribute in your simulation):
    Ethnic Hungarians are more likely to be Roman Catholic or Protestant.
    Ethnic Romanians are predominantly Orthodox.

Age:
    Younger generations in urban areas are more likely to identify as atheist or agnostic.
"""




def calculate_orthodox_probability(residence, age):
    """Calculate probability of being Orthodox Christian."""
    base_probability = 0.85  # Nationwide average
    if residence == "urban":
        base_probability -= 0.1  # Slightly lower in urban areas
    if age < 30:
        base_probability -= 0.05  # Slightly lower for younger generations
    return max(0.0, base_probability)


def calculate_catholic_probability(residence, age):
    """Calculate probability of being Roman Catholic."""
    base_probability = 0.05  # Nationwide average
    if residence == "urban":
        base_probability += 0.02  # Slightly higher in urban areas
    return max(0.0, base_probability)


def calculate_protestant_probability(residence, age):
    """Calculate probability of being Protestant."""
    base_probability = 0.03  # Nationwide average
    if residence == "urban":
        base_probability += 0.01  # Slightly higher in urban areas
    return max(0.0, base_probability)


def calculate_other_probability(residence, age):
    """Calculate probability of belonging to 'Other' religions."""
    base_probability = 0.07  # Nationwide average
    if residence == "urban":
        base_probability += 0.07  # More diversity in urban areas
    if age < 30:
        base_probability += 0.03  # Younger people are more likely to identify as atheist/agnostic
    return max(0.0, base_probability)


def assign_religion(person: Person):
    """Assign religion to a person."""
    p_orthodox = calculate_orthodox_probability(person.residence, person.age)
    p_catholic = calculate_catholic_probability(person.residence, person.age)
    p_protestant = calculate_protestant_probability(person.residence, person.age)
    p_other = calculate_other_probability(person.residence, person.age)

    # Normalize probabilities to ensure they sum to 1
    total = p_orthodox + p_catholic + p_protestant + p_other
    p_orthodox /= total
    p_catholic /= total
    p_protestant /= total
    p_other /= total

    # Generate a random number and assign religion
    r = random()
    if r < p_orthodox:
        person.religion = Religion.ORTHODOX
    elif r < p_orthodox + p_catholic:
        person.religion = Religion.CATHOLIC
    elif r < p_orthodox + p_catholic + p_protestant:
        person.religion = Religion.PROTESTANT
    else:
        person.religion = Religion.OTHER
