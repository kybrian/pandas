import pandas as pd 

# Increase the maximum number of rows to display the entire dataframe
pd.options.display.max_rows = 9999

df = pd.read_csv("data.csv") 

# Print a csv
# print(df.to_string())

# number of rows returned
# print(f"No of rows returned: {pd.options.display.max_rows}")

print(df)
