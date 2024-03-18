from enum import Enum

# personality type class of all the possible types of personalities a user can generate.
# the class Personality is an Enum. The attributes Personality.DOMINANCE, Personality.INFLUENCE, etc., are enumeration members (or members) and are functionally constants.
#The enum members have names and values (the name of Personality.DOMINANCE is DOMINANCE, the value of Personality.INFLUENCE is 2, etc.)

class PersonalityType(Enum):
    DOMINANCE = 1
    INFLUENCE = 2
    STEADY = 3
    CONSCIENTIOUS = 4