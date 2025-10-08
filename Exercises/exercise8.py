import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import openpyxl

df = pd.read_csv('train_viz.csv')

plt.scatter(x=df['duration'], y=df['price'])
plt.xlabel('duration (m)')
plt.ylabel('price (£)')
plt.show()
