import pandas as pd 

# Return a new DataFrame with no empty cells 

df = pd.read_csv("dataset.csv")

# new_df = df.dropna(inplace=True)

df.fillna(130, inplace=True)

print(new_df.to_string())

