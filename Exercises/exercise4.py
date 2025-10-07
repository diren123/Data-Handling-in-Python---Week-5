import numpy as np
import scipy.stats

x = np.arange(10)
print(x)

# 1.
# Display the first five elements
print(x[:5])

# 2.
# Display every other element
print(x[::2])

# 3.
# Display the elements from index 5 in reverse order
print(x[5::-1])

# two dimensional array
y = np.array([[12, 5, 2, 4],
              [ 7, 6, 8, 8],
              [ 1, 6, 7, 7]])

# 4.
# Display the first 2 rows and the first 3 columns.
print("Displaying the first 2 rows and the first 3 columns: ")
print(y[:2, :3])

# 5.
# Display the first column of y
print("Displaying the first column of y")
print(y[:,0])

# 6.
# Display the first row of y
print("Displaying the first row of y")
print(y[0,:])

# 7.
# Read the contents of file cdc_1.csv, containing heights, weights and
# ages, into array data. To do this, you can use the below code:
# data = np.genfromtxt('data/cdc_1.csv', delimiter=',', skip_header=1)

data = np.genfromtxt('cdc_1.xls', delimiter=',', skip_header=1)

# 8.
# Calculate the minimum, maximum, and mean height, weight, and age
print("The minimum height, weight and age are: ")
print(data.min(axis = 0))

print("The maximum height, weight and age are: ")
print(data.max(axis = 0))

print("The mean height, weight and age are: ")
print(data.mean(axis = 0))

# Descriptive statistics with NumPy

# 1.
# Read the contents of file cdc_nan.csv, containing heights, weights and
# ages, into array data. To do this, you can use the below code:
# data = np.genfromtxt('data/cdc_nan.csv', delimiter=',', skip_header=1)

data = np.genfromtxt('cdc_nan.xls', delimiter=',', skip_header=1)
heights = data[:,0]
weights = data[:,1]
print("Heights are: ", heights)
print("Weights are: ", weights)

# Univariate
# Measures of central tendency

# Median

# 1.
# Calculate the median for the heights and the weights and assign the
# values to variables.
median_heights = np.median(heights)
print("Median Heights are: ", median_heights)

median_weights = np.median(weights)
print("Median Weights are: ", median_weights)

# 2.
# What has happened? Check if the arrays contain missing values
print(np.isnan(heights))

print(np.sum(np.isnan(heights)))

print(np.isnan(weights))

print(np.sum(np.isnan(weights)))

# 3.
# Array weights contain three nan values. Find their positions.
print("Positions of the three nan values: ", np.argwhere(np.isnan(weights)))

# 4.
# Now calculate the median for the weights ignoring the nan values
median_weights = np.nanmedian(weights)
print("Median for the weights ignoring the nan values: ", median_weights)

# Mean
# Calculate the mean values for the heights and weights
median_heights = np.mean(heights)
print("Median Heights are: ", median_heights)

median_weights = np.nanmean(weights)
print("Median Weights are: ", median_weights)

# Range
# Calculate the range of the heights and the weights. Remember, range is the
# difference between the maximum and the minimum value.
range_heights = np.max(heights) - np.min(heights)
print("The Range is:", range_heights)

range_weights = np.max(weights) - np.min(weights)
print("The Range is: ", range_weights)

range_weights = np.nanmax(weights) - np.nanmin(weights)
print("The Range is: ", range_weights)

# Interquartile Range (IQR)
# Find the quartiles for the heights and the weights, and the Interquartile
# Range (IQR)
quartile_heights = np.quantile(heights, [0.25, 0.5, 0.75])
print("Quartile Heights: ", quartile_heights)

iqr_heights = quartile_heights[2] - quartile_heights[0]
print("The Interquartile Range is: ", iqr_heights)

quartile_weights = np.quantile(weights, [0.25, 0.5, 0.75])
print("Quartile Weights: ", quartile_weights)

quartile_weights = np.nanquantile(weights, [0.25, 0.5, 0.75])
iqr_weights = quartile_weights[2] - quartile_weights[0]
print("The Interquartile Range is: ", iqr_weights)

