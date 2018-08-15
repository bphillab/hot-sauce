from enum import Enum, auto


class Peppers(Enum):
    BANANA = auto()
    JALAPENO = auto()
    GUAJILLO = auto()
    CAYENNE = auto()
    HABANERO = auto()
    RED_SAVINA = auto()
    NAGA_VIPER = auto()


PEPPER_FACTORS = {
   Peppers.BANANA: 1.0,
   Peppers.JALAPENO: 5.0,
   Peppers.GUAJILLO: 5.0,
   Peppers.CAYENNE: 10.0,
   Peppers.HABANERO: 25.0,
   Peppers.RED_SAVINA: 40.0,
   Peppers.NAGA_VIPER: 60.0
}

PEPPER_PROBABILITIES = {
   Peppers.BANANA: (0.1, 0.9),
   Peppers.JALAPENO: (0.4, 0.6),
   Peppers.GUAJILLO: (0.1, 0.9),
   Peppers.CAYENNE: (0.4, 0.6),
   Peppers.HABANERO: (0.5, 0.5),
   Peppers.RED_SAVINA: (0.1, 0.9),
   Peppers.NAGA_VIPER: (0.05, 0.95)
}

GREEN_PEPPERS = [
    Peppers.BANANA,
    Peppers.JALAPENO,
]
GREEN_PEPPER_COLOR_MODE = 0.25
GREEN_PEPPER_COLOR_SHAPE = 1.1

RED_PEPPERS = [
    Peppers.GUAJILLO,
    Peppers.CAYENNE,
    Peppers.HABANERO,
    Peppers.RED_SAVINA,
    Peppers.NAGA_VIPER
]
RED_PEPPER_COLOR_MODE = 0.75
RED_PEPPER_COLOR_SHAPE = 1.1

AGE_Y_SCALE = 20.0
AGE_X_SCALE = 0.2 
