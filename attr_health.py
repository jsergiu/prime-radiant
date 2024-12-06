import random

from .person import Person

"""
Categories for Health Status

We define four health statuses:

Healthy: No major chronic conditions, fit for most activities.
Minor Conditions: Mild issues (e.g., seasonal allergies, mild hypertension).
Chronic Conditions: Ongoing illnesses (e.g., diabetes, heart disease).
Severe/Disabled: Significant health issues or disabilities limiting daily activities.

Key Influencing Factors

Age:
    Younger individuals are generally healthier.
    Older individuals are more likely to have chronic or severe conditions.
Residence:
    Rural populations have less access to healthcare and higher rates of untreated conditions.
    Urban populations have better access to healthcare and preventive services.
Income:
    Higher income is associated with better health outcomes.
    Lower income correlates with higher rates of chronic and severe conditions.
Education:
    Higher education correlates with better health awareness and preventive care.
Gender (minor influence):
    Women may report health issues more frequently but live longer.
    Men may have higher rates of severe health issues due to lifestyle factors.
"""

from random import random
from .person import Person
from .enums import HealthStatus


def calculate_healthy_probability(age, residence, income, education):
    """Calculate probability of being healthy."""
    base_probability = 0.7  # General baseline
    if age < 30:
        base_probability += 0.2  # Younger people are healthier
    elif age >= 60:
        base_probability -= 0.3  # Older age reduces health probability

    if residence == "rural":
        base_probability -= 0.1  # Rural areas have less access to healthcare

    if income == "high":
        base_probability += 0.1  # Higher income boosts health
    elif income == "low":
        base_probability -= 0.1

    if education in ["Undergraduate", "Postgraduate"]:
        base_probability += 0.1  # Higher education improves health awareness

    return max(0.0, base_probability)


def calculate_minor_conditions_probability(age, residence):
    """Calculate probability of having minor health conditions."""
    base_probability = 0.2  # General baseline
    if age >= 30 and age < 60:
        base_probability += 0.2  # Middle-aged individuals likely to have mild conditions

    if residence == "rural":
        base_probability += 0.05  # Less healthcare access may increase mild issues

    return max(0.0, base_probability)


def calculate_chronic_conditions_probability(age, income):
    """Calculate probability of having chronic health conditions."""
    base_probability = 0.1  # General baseline
    if age >= 40:
        base_probability += 0.3  # Chronic issues more likely with age

    if income == "low":
        base_probability += 0.1  # Lower income correlates with higher chronic disease rates

    return max(0.0, base_probability)


def calculate_severe_disabled_probability(age, income):
    """Calculate probability of being severely disabled or having severe conditions."""
    base_probability = 0.05  # General baseline
    if age >= 60:
        base_probability += 0.3  # Older populations are more likely to have severe issues

    if income == "low":
        base_probability += 0.1  # Low income correlates with severe conditions

    return max(0.0, base_probability)


def assign_health(person: Person):
    """Assign health status to a person."""
    p_healthy = calculate_healthy_probability(person.age, person.residence, person.income, person.education)
    p_minor = calculate_minor_conditions_probability(person.age, person.residence)
    p_chronic = calculate_chronic_conditions_probability(person.age, person.income)
    p_severe = calculate_severe_disabled_probability(person.age, person.income)

    # Normalize probabilities to ensure they sum to 1
    total = p_healthy + p_minor + p_chronic + p_severe
    p_healthy /= total
    p_minor /= total
    p_chronic /= total
    p_severe /= total

    # Generate a random number to assign health status
    r = random()
    if r < p_healthy:
        person.health_status = HealthStatus.HEALTHY
    elif r < p_healthy + p_minor:
        person.health_status = HealthStatus.MINOR_CONDITIONS
    elif r < p_healthy + p_minor + p_chronic:
        person.health_status = HealthStatus.CHRONIC_CONDITIONS
    else:
        person.health_status = HealthStatus.SEVERELY_DISABLED
