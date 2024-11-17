"""Data Cleaning."""

import random
import numpy as np
import pandas as pd


df = pd.read_csv('/Users/glebtrofimov/Downloads/life_expectancy.csv')

df

# ![handling-missing-values-diagram_xr4ryx.png](attachment:handling-missing-values-diagram_xr4ryx.png)

# # Dealing with missing data

# Missing data can arise in the dataset due to multiple reasons: the data for the specific field was not added by the user/data collection application, data was lost while transferring manually, a programming error, etc. 
#
# For numerical data, pandas uses a floating point value NaN (Not a Number) to represent missing data. It is a unique value defined under the library Numpy so we will need to import it as well. NaN is the default missing value marker for reasons of computational speed and convenience. This is a sentinel value, in the sense that it is a dummy data or flag value that can be easily detected and worked with using functions in pandas.

series = pd.Series([1, 2, 3, 4, 5, np.nan, 6, 7, 8, 9, 0])
series

series.mean()

series.isnull()

series = series.dropna() # removing all the NaNs
series

series.isnull()

series.mean()

data = {'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
        'condition': ['serious', 'serious', np.nan, 'stable', np.nan,
                      'stable', 'stable', 'serious', 'serious', np.nan, 'stable', np.nan]}

machine_cdtn = pd.DataFrame(data)
machine_cdtn

machine_cdtn.dropna(axis=0) # removes NaNs row-wise

machine_cdtn.dropna(axis=1) # removes NaNs column-wise

# only removes columns that contain nothing but NaNs
machine_cdtn.dropna(how='all')

# # Filling in Missing Data

machine_cdtn.fillna('unknown')

# # Data Transformation

# # Applying to a real dataframe

df

# lets make the missing data visible

df_na = df[df.isna().any(axis=1)]
df_na

# lets replace Hepatitis column's missing values with the average value

df['Hepatitis B'] = df['Hepatitis B'].fillna(df['Hepatitis B'].mean())
df

# +
# also we can replace NaNs in every column with its unique value

# data_dim_fill = data_dim.fillna({0: 0, 1: 8, 2: 9, 3: 10})
#ndata_dim_fill
# -

# # Replacing Values

# +
data1 = pd.Series([1,2,-99,4,5,-99,7,8,-99])

data1

# -

# Replace the placeholder -99 as NaN
data1.replace(-99, np.nan)


# # Concatenating Pandas Series

# Create a new Series
new_data = pd.Series([-100, 11, 12, 13])
combined_series = pd.concat([data1, new_data], ignore_index = True)
combined_series


# Let's replace -99 and -100 as NaN in the new combined_series
data_replaced = combined_series.replace([-99, -100], np.nan)
data_replaced


# # Map Function

data_number = pd.DataFrame({'english': ['zero','one','two',
                                        'three','four', 'five'],
                            'digits': [0,1,2,3,4,5]})
data_number

# +
english_to_multiple = {
    'two': 'yes',
    'four': 'yes'
}

data_number['multiple'] = data_number['english'].map(english_to_multiple)
data_number


# -

# # Discretization - Cut Function

# +
data3 = random.sample(range(1, 101), 30)

data4 = pd.cut(data3, 5)
data4

# -

df
