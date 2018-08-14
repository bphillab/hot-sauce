import numpy as np
import pandas as pd

from hot_sauce.config import (
    Peppers,
    PEPPER_FACTORS,
    PEPPER_PROBABILITIES,
    GREEN_PEPPERS,
    GREEN_PEPPER_COLOR_MODE,
    GREEN_PEPPER_COLOR_SHAPE,
    RED_PEPPERS,
    RED_PEPPER_COLOR_MODE,
    RED_PEPPER_COLOR_SHAPE,
    AGE_X_SCALE,
    AGE_Y_SCALE
)


class HotSauceData:

    def sample(self, n):
        peppers = sample_peppers(n)
        peppers_df = enum_to_data_frame(Peppers, peppers)
        peppers_factor = compute_peppers_factor(peppers_df)
        color = compute_color(peppers)
        ages = sample_ages(n)
        age_factor = compute_age_factor(ages)
        hotness = peppers_factor + age_factor
        return pd.concat([peppers_df, ages, hotness], axis=1)


def sample_peppers(n):
    return [[Peppers.JALAPENO] for _ in range(n)]

def enum_to_data_frame(enum, list_of_enum_values):
    return pd.Series([1]*len(list_of_enum_values))

def compute_peppers_factor(peppers_df):
    return pd.Series([0.5]*len(peppers_df))

def compute_color(peppers_df):
    return pd.Series([0.5]*len(peppers_df))

def sample_ages(n):
    return pd.Series([5]*n)

def compute_age_factor(ages):
    return pd.Series([1]*len(ages))


#    commute_time_raw = (
#        RAW_DISTANCE_SLOPE * raw_distance
#            - RAW_DISTANCE_NONLINEARITY_Y_SCALE * (
#                2 / (1 + np.exp(RAW_DISTANCE_NONLINEARITY_X_SCALE * raw_distance)
#                         ** RAW_DISTANCE_NONLINEARITY_POWER))
#            + TIME_OF_DAY_FACTOR_SCALING * time_of_day_factor
#            + geometry_factor
#            + commute_type_factor)
