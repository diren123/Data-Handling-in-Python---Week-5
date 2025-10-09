import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1.
# Load in the dataset train_viz.csv
df = pd.read_csv('train_viz.csv')

# 2.
# Create a scatter plot of duration vs. price.
# Segment by destination
plt.scatter(x=df['duration'], y=df['price'])
plt.xlabel('duration (m)')
plt.ylabel('price (£)')
plt.show()

sns.scatterplot(data=df,
                x='duration',
                y='price',
                hue='destination'
                )
plt.show()

# 3.
# Create a barplot of fare counts
plt.bar(x=df['fare'].unique(),
        height=df['fare'].value_counts())
plt.ylabel('price (£)')
plt.xticks(rotation = 60)
plt.show()

# 4.
# Create a box and whisker plot of price with
# respect to destination
sns.boxplot(data=df,
            x='destination',
            y='price'
            )
plt.show()

# 5.
# Create a histogram of duration
sns.histplot(data=df,
             x='duration'
             )
plt.show()

plt.hist(df['duration'])
plt.show()
