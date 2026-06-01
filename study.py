import numpy as np

stocks = np.array([
    [100, 120, 150],  # День 0 (Пн)
    [102, 118, 155],  # День 1 (Вт)
    [105, 122, 160],  # День 2 (Ср)
    [110, 125, 165]   # День 3 (Чт)
])

risk_match = stocks[:, 0] > 103
high_value_mask = stocks[:, 1] > 120
print(stocks[risk_match, 0])
print(stocks[high_value_mask])