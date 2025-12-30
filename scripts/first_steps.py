import pandas as pd

ages = pd.Series(
    [18, 21, 19, 22],
    index=["Alice", "Bob", "Charlie", "Diana"]
)
print("Series example:")
print(ages)
print()

data = {
    "stop_name": ["Central Station", "Main Square", "City Park"],
    "lines": [5, 3, 2]
}

df = pd.DataFrame(data)
print("DataFrame example:")
print(df)
print()

print("Head:")
print(df.head())
print()

print("Info:")
print(df.info())
