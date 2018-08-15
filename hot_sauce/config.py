from enum import Enum, auto


class Peppers(Enum):
    BANANA = auto()
    POBLANO = auto()
    JALAPENO = auto()
    GUAJILLO = auto()
    CAYENNE = auto()
    HABANERO = auto()
    NAGA_VIPER = auto()


PEPPER_FACTORS = {
   Peppers.BANANA: 1.0,
   Peppers.POBLANO: 5.0,
   Peppers.JALAPENO: 10.0,
   Peppers.GUAJILLO: 15.0,
   Peppers.CAYENNE: 20.0,
   Peppers.HABANERO: 30.0,
   Peppers.NAGA_VIPER: 40.0
}

PEPPER_PROBABILITIES = {
   Peppers.BANANA: (0.3, 0.7),
   Peppers.POBLANO: (0.2, 0.8),
   Peppers.JALAPENO: (0.6, 0.4),
   Peppers.GUAJILLO: (0.1, 0.9),
   Peppers.CAYENNE: (0.4, 0.6),
   Peppers.HABANERO: (0.4, 0.6),
   Peppers.NAGA_VIPER: (0.1, 0.9)
}

GREEN_PEPPERS = [
    Peppers.BANANA,
    Peppers.JALAPENO,
    Peppers.POBLANO
]
GREEN_PEPPER_COLOR_MODE = 0.25
GREEN_PEPPER_COLOR_SHAPE = 1.1

RED_PEPPERS = [
    Peppers.GUAJILLO,
    Peppers.CAYENNE,
    Peppers.HABANERO,
    Peppers.NAGA_VIPER
]
RED_PEPPER_COLOR_MODE = 0.75
RED_PEPPER_COLOR_SHAPE = 1.1

AGE_Y_SCALE = 40.0
AGE_X_SCALE = 0.3 
