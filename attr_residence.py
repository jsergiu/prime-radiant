from random import random
from .person import Person
from .enums import Residence, Region

# Regional data with population percentages and urbanization levels
REGIONAL_DATA = {
    "NORD_EST": {"population_percentage": 0.193, "urban_percentage": 45},
    "SUD_EST": {"population_percentage": 0.146, "urban_percentage": 50},
    "SUD_MUNTENIA": {"population_percentage": 0.170, "urban_percentage": 40},
    "SUD_VEST_OLTENIA": {"population_percentage": 0.117, "urban_percentage": 45},
    "VEST": {"population_percentage": 0.105, "urban_percentage": 54},
    "NORD_VEST": {"population_percentage": 0.141, "urban_percentage": 50},
    "CENTRU": {"population_percentage": 0.131, "urban_percentage": 51},
    "BUCURESTI_ILFOV": {"population_percentage": 0.117, "urban_percentage": 90},
}

def assign_residence(person: Person):
    """Assigns residence (urban or rural) based on regional population percentages and urbanization levels."""
    # Choose region based on population percentage
    r = random()
    cumulative_probability = 0.0
    for region_name, data in REGIONAL_DATA.items():
        cumulative_probability += data["population_percentage"]
        if r < cumulative_probability:
            person.region = Region[region_name.upper().replace("-", "_").replace(" ", "_")]
            break

    # Urban or Rural within the chosen region
    urban_percentage = REGIONAL_DATA[person.region.name]["urban_percentage"] / 100
    rural_percentage = 1 - urban_percentage

    # Adjust rural probability inversely proportional to age (older people more likely rural)
    rural_probability = rural_percentage + 0.2 * (person.age / 99)
    urban_probability = 1 - rural_probability

    residence_probabilities = {
        Residence.URBAN: urban_probability,
        Residence.RURAL: rural_probability,
    }

    # Assign residence based on probabilities
    r = random()
    cumulative_probability = 0.0
    for residence, probability in residence_probabilities.items():
        cumulative_probability += probability
        if r < cumulative_probability:
            person.residence = residence
            break
