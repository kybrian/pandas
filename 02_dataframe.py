import pandas as pd

data = {
    'calories' : [420, 380, 390],
    'duration' : [50, 40, 45]
}

df = pd.DataFrame(data)

# print(df)

# print(f"Row 1 : \n {df.loc[0]}")

df = pd.DataFrame(data, index = ['day1','day2','day3'])

print(df)