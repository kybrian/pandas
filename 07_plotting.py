import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('plot.csv')

# df.plot()

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

df["Duration"].plot(kind = 'hist')

plt.show()