import pandas as pd 

# Create a series from a list 

a = [1, 7, 2]

myVar = pd.Series(a) 

print(myVar)

# Create a label using index 
myVar = pd.Series(a, index= ['x', 'y', 'z'])

print(myVar)

# Accessing a label
print(myVar['x'])

# Key Value Objects as Series 
calories = {"day1": 420, "day2": 380, "day3": 390}

myVar = pd.Series(calories) 

print(myVar)

myVar = pd.Series(calories, index=['day1', 'day2'])

print(myVar)