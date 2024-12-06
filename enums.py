from enum import Enum

class MaritalStatus(Enum):
    NEVER_MARRIED = 1
    MARRIED = 2
    WIDOW = 3

class EducationLevel(Enum):
    NONE = 1 # no formal education
    PRIMARY = 2 # elementary
    SECONDARY = 3 # high school
    UNDERGRADUATE = 4 # college, batchelor's degree
    POSTGRADUATE = 5 # master's degree, doctorate

class EmploymentStatus(Enum):
    UNDEFINED = 0
    TOO_YOUNG = 1
    STUDENT = 2
    EMPLOYED = 3
    UNEMPLOYED = 4
    RETIRED = 5

class Residence(Enum):
    UNDEFINED = 0
    RURAL = 1
    URBAN = 2

class Region(Enum):
    UNDEFINED = 0
    NORD_EST = 1
    SUD_EST = 2
    SUD_MUNTENIA = 3
    SUD_VEST_OLTENIA = 4
    VEST = 5
    NORD_VEST = 6
    CENTRU = 7
    BUCURESTI_ILFOV = 8

class Religion(Enum):
    UNDEFINED = 0
    ORTHODOX = 1
    CATHOLIC = 2
    PROTESTANT = 3
    OTHER = 4
    
class Ethnicity(Enum):
    UNDEFINED = 0
    ROMANIAN = 1
    HUNGARIAN = 2
    ROMA = 3
    OTHER = 4

class HealthStatus(Enum):
    HEALTHY = 1
    MINOR_CONDITIONS = 2
    CHRONIC_CONDITIONS = 3
    SEVERELY_DISABLED = 4

class PoliticalAffiliation(Enum):
    CONSERVATIVE = 1
    LIBERAL = 2 
    CENTRIST = 3
    APOLITICAL = 4
    EXTREMIST = 5

class TechnologyUse(Enum):
    NON_USER = 1
    BASIC_USER = 2
    SOCIAL_MEDIA_USER = 3
    ADVANCED_USER = 4