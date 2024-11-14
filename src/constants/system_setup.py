from enum import Enum

class SystemSetup(Enum):
    BASIC = {"plan": "Basic", "max_batteries": 2}
    STANDARD = {"plan": "Standard", "max_batteries": 3}
    PRO = {"plan": "Pro", "max_batteries": 5}