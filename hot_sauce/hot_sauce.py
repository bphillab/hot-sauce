import numpy as np
import pandas as pd

from hot_sauce.utils import (
    remove_nones,
    enum_to_data_frame,
    sample_gamma,
    sample_beta_green,
    sample_beta_red
)

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
        spicyness = pd.Series(
            peppers_factor + age_factor + sample_gamma(mode=1.0, shape=2.0, n=n),
            name='SPICYNESS')
        return pd.concat([peppers_df, color, ages, spicyness], axis=1)


def sample_peppers(n):
    peppers = []
    for _ in range(n):
        row = [
            np.random.choice(
                [pepper, None], 
                p=PEPPER_PROBABILITIES[pepper])
            for pepper in Peppers]
        row = remove_nones(row)
        if row == []:
            row = [np.random.choice(Peppers)]
        peppers.append(row)
    return peppers

def compute_peppers_factor(peppers_df):
    n = len(peppers_df)
    spicyness_levels = np.concatenate([
            np.repeat(PEPPER_FACTORS[p], repeats=n).reshape(-1, 1)
            for p in Peppers],
        axis=1)
    spicyness_contribution = spicyness_levels * peppers_df.values
    # Only the two spicyest peppers contribute to the spice level of the sauce.
    spicyness = np.sort(spicyness_contribution, axis=1)[:, -3:]
    return np.sum(spicyness, axis=1)

def compute_color(peppers):
    colors = []
    for row in peppers:
        green_color = sum(
            sample_beta_green(1)[0] for p in row if p in GREEN_PEPPERS)
        red_color = sum(
            sample_beta_red(1)[0] for p in row if p in RED_PEPPERS)
        color = (green_color + red_color) / len(row)
        colors.append(color)
    return pd.Series(colors, name='COLOR')

def sample_ages(n):
    return pd.Series(sample_gamma(n, mode=5.0, shape=5.0), name='AGE')

def compute_age_factor(age):
    age_factor = (
        AGE_Y_SCALE - AGE_Y_SCALE * (2 / (1 + np.exp(AGE_X_SCALE * age))))
    return age_factor
