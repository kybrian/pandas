import pandas as pd

mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings' : [3, 7, 2]
}

myVar = pd.DataFrame(mydataset)

print(myVar)
print()

print(f"Pandas Version: {pd.__version__}")