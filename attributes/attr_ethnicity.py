from random import random
from .person import Person
from .enums import Ethnicity


"""
Major Ethnic Groups in Romania
Romanian (~89% of the population)
Hungarian (~6%)
Roma (Gypsy) (~3%)
Other (~2%, including Germans, Ukrainians, Turks, Tatars, Russians, and others)

Key Influencing Factors

Residence:
    Rural areas have a higher concentration of Roma and Hungarian populations.
    Urban areas are predominantly Romanian, with small percentages of other ethnicities.

Region:
    Hungarians are concentrated in Transylvania and parts of the North-West region.
    Germans are found in Transylvania and Banat.
    Roma populations are dispersed but more concentrated in certain rural areas.

Age (Minor influence):
    Younger generations in urban areas may identify more with "Other" or mixed ethnicities.
"""



def calculate_romanian_probability(residence, region):
    """Calculate probability of being Romanian."""
    base_probability = 0.89  # Nationwide average
    if region in ["Transylvania", "Banat"]:
        base_probability -= 0.05  # Higher diversity in these regions
    if residence == "rural":
        base_probability += 0.02  # Rural areas are predominantly Romanian
    return max(0.0, base_probability)


def calculate_hungarian_probability(residence, region):
    """Calculate probability of being Hungarian."""
    base_probability = 0.06  # Nationwide average
    if region in ["Transylvania", "North-West"]:
        base_probability += 0.15  # High concentration of Hungarians
    if residence == "urban":
        base_probability -= 0.02  # Slightly lower in urban areas
    return max(0.0, base_probability)


def calculate_roma_probability(residence, region):
    """Calculate probability of being Roma."""
    base_probability = 0.03  # Nationwide average
    if residence == "rural":
        base_probability += 0.05  # Higher concentration in rural areas
    if region in ["South", "South-East"]:
        base_probability += 0.02  # Higher Roma populations in these regions
    return max(0.0, base_probability)


def calculate_other_probability(residence, region):
    """Calculate probability of being 'Other'."""
    base_probability = 0.02  # Nationwide average
    if region in ["Transylvania", "Banat"]:
        base_probability += 0.03  # More Germans and Ukrainians in these regions
    if residence == "urban":
        base_probability += 0.01  # Slightly higher diversity in urban areas
    return max(0.0, base_probability)


def assign_ethnicity(person: Person):
    """Assign ethnicity to a person."""
    p_romanian = calculate_romanian_probability(person.residence, person.region)
    p_hungarian = calculate_hungarian_probability(person.residence, person.region)
    p_roma = calculate_roma_probability(person.residence, person.region)
    p_other = calculate_other_probability(person.residence, person.region)

    # Normalize probabilities to ensure they sum to 1
    total = p_romanian + p_hungarian + p_roma + p_other
    p_romanian /= total
    p_hungarian /= total
    p_roma /= total
    p_other /= total

    # Generate a random number and assign ethnicity
    r = random()
    if r < p_romanian:
        person.ethnicity = Ethnicity.ROMANIAN
    elif r < p_romanian + p_hungarian:
        person.ethnicity = Ethnicity.HUNGARIAN
    elif r < p_romanian + p_hungarian + p_roma:
        person.ethnicity = Ethnicity.ROMA
    else:
        person.ethnicity = Ethnicity.OTHER
