import pandas as pd

df = pd.read_csv("data/transport.csv")

print("Missing values:")
print(df.isna().sum())
print()

df["lines"] = df["lines"].fillna(0)

df = df.rename(columns={
    "stop_name": "stop",
    "lines": "number_of_lines"
})

df["number_of_lines"] = df["number_of_lines"].astype(int)

print("Cleaned data:")
print(df)
