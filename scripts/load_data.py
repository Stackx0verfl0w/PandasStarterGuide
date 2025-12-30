import pandas as pd

df = pd.read_csv("data/transport.csv")

print("Loaded data:")
print(df.head())
print()

print("Info:")
print(df.info())
print()

print("Statistics:")
print(df.describe())
