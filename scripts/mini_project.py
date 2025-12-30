import pandas as pd

df = pd.read_csv("data/transport.csv")

print(df.info())
print()

df["lines"] = df["lines"].fillna(0)
df = df.rename(columns={
    "stop_name": "stop",
    "lines": "number_of_lines"
})
df["number_of_lines"] = df["number_of_lines"].astype(int)

lines_per_zone = df.groupby("zone")["number_of_lines"].sum()
print("Lines per zone:")
print(lines_per_zone)

lines_per_zone.to_csv("data/lines_per_zone.csv")
print("Results exported to data/lines_per_zone.csv")
