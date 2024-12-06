from random import random
from .person import Person
from .enums import PoliticalAffiliation

"""
Categories for Political Affiliation

    Conservative
    Liberal
    Centrist
    Apolitical
    Extremist (Far-right or Far-left)

Key Influencing Factors for Extremism

Age:
    Younger individuals (18–35) are more likely to align with extremist ideologies, often due to dissatisfaction with the status quo.
Residence:
    Rural areas may lean toward extremism due to economic hardship and less access to diverse political discourse.
Income:
    Low-income individuals are more likely to feel disenfranchised and gravitate toward extremist views.
Education:
    Lower education levels correlate with susceptibility to extremist rhetoric.
Global Trends:
    Current studies suggest that ~20% of Romanians support extremist ideologies (far-right or far-left).
"""





def calculate_conservative_probability(age, residence, income, education):
    """Calculate probability of being conservative."""
    base_probability = 0.35  # Adjusted to accommodate extremism
    if age >= 50:
        base_probability += 0.2
    elif age < 30:
        base_probability -= 0.1

    if residence == "rural":
        base_probability += 0.2

    if income == "low":
        base_probability += 0.1

    if education in ["Undergraduate", "Postgraduate"]:
        base_probability -= 0.1

    return max(0.0, base_probability)


def calculate_liberal_probability(age, residence, income, education):
    """Calculate probability of being liberal."""
    base_probability = 0.25  # Adjusted to accommodate extremism
    if age < 30:
        base_probability += 0.2
    elif age >= 50:
        base_probability -= 0.1

    if residence == "urban":
        base_probability += 0.2

    if income == "high":
        base_probability += 0.1

    if education in ["Undergraduate", "Postgraduate"]:
        base_probability += 0.1

    return max(0.0, base_probability)


def calculate_centrist_probability(age, residence, income, education):
    """Calculate probability of being centrist."""
    base_probability = 0.15  # Adjusted to accommodate extremism
    if age >= 30 and age < 50:
        base_probability += 0.1

    if residence == "urban":
        base_probability += 0.05

    if education in ["Undergraduate", "Postgraduate"]:
        base_probability += 0.1

    return max(0.0, base_probability)


def calculate_apolitical_probability(age, residence):
    """Calculate probability of being apolitical."""
    base_probability = 0.05  # Adjusted to accommodate extremism
    if age < 30:
        base_probability += 0.1

    if residence == "rural":
        base_probability -= 0.05

    return max(0.0, base_probability)


def calculate_extremist_probability(age, residence, income, education):
    """Calculate probability of being extremist."""
    base_probability = 0.2  # Approximately 20% of the population
    if age < 35:
        base_probability += 0.1  # Younger people are more prone to extremism
    if residence == "rural":
        base_probability += 0.05
    if income == "low":
        base_probability += 0.1
    if education in ["Undergraduate", "Postgraduate"]:
        base_probability -= 0.1

    return max(0.0, base_probability)


def assign_political_affiliation(person: Person):
    """Assign political affiliation to a person."""
    p_conservative = calculate_conservative_probability(person.age, person.residence, person.income, person.education)
    p_liberal = calculate_liberal_probability(person.age, person.residence, person.income, person.education)
    p_centrist = calculate_centrist_probability(person.age, person.residence, person.income, person.education)
    p_apolitical = calculate_apolitical_probability(person.age, person.residence)
    p_extremist = calculate_extremist_probability(person.age, person.residence, person.income, person.education)

    # Normalize probabilities to ensure they sum to 1
    total = p_conservative + p_liberal + p_centrist + p_apolitical + p_extremist
    p_conservative /= total
    p_liberal /= total
    p_centrist /= total
    p_apolitical /= total
    p_extremist /= total

    # Generate a random number to assign political affiliation
    r = random()
    if r < p_conservative:
        person.political_affiliation = PoliticalAffiliation.CONSERVATIVE
    elif r < p_conservative + p_liberal:
        person.political_affiliation = PoliticalAffiliation.LIBERAL
    elif r < p_conservative + p_liberal + p_centrist:
        person.political_affiliation = PoliticalAffiliation.CENTRIST
    elif r < p_conservative + p_liberal + p_centrist + p_apolitical:
        person.political_affiliation = PoliticalAffiliation.APOLITICAL
    else:
        person.political_affiliation = PoliticalAffiliation.EXTREMIST
