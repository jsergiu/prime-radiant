import random
from datetime import datetime

from .enums import EducationLevel, EmploymentStatus, Ethnicity, HealthStatus, MaritalStatus, PoliticalAffiliation, Region, Religion, Residence, TechnologyUse

class Person:
    age: int
    education: EducationLevel
    employment: EmploymentStatus
    ethnicity: Ethnicity
    gender: str
    health: HealthStatus
    income: int
    marital_status: str
    political_affiliation: PoliticalAffiliation
    pregnant: str
    religion: Religion
    region: Region
    residence: Residence
    residence: str
    technology_use: TechnologyUse


    def __init__(self):
        self.age = 0
        self.education = EducationLevel.NONE
        self.employment = EmploymentStatus.UNDEFINED
        self.ethnicity = Ethnicity.UNDEFINED
        self.gender = 0
        self.health = 0
        self.income = 0
        self.region = Region.UNDEFINED
        self.marital_status = MaritalStatus.NEVER_MARRIED
        self.political_affiliation = 0
        self.pregnant = False
        self.religion = Religion.UNDEFINED
        self.residence = Residence.UNDEFINED
        self.technology_use = 0
        
    
    def __repr__(self):
        return f"{str(self.gender).ljust(10)} | {str(self.age).ljust(5)} | {str(self.marital_status.name).ljust(15)} | {str(self.residence).ljust(5)}"
    
