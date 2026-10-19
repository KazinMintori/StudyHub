"""Đọc cấu trúc Palmer Penguins. Chạy: python penguins.py"""

import pandas as pd

url = (
    "https://raw.githubusercontent.com/"
    "allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
)
penguins = pd.read_csv(url)

print(penguins.head())
print()
print(penguins.shape)
print()
print(penguins.columns)
print()
print(penguins.dtypes)
