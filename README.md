# Simulated Pepper Sauce Spicyness Dataset

This contains a simulation engine for creating hot sauce spicyness data.

## Insallation

To install in development mode:

```
git clone https://github.com/madrury/hot-sauce.git
cd commute-times
pip install -e .
```

## Use

To simulate a 5000 record data set:

```
from hot_sauce.hot_sacue import HotSauceData
hot_sauce_data = HotSauceData().sample(5000)
```
