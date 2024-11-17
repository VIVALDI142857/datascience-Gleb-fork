"""Fixing wrong data with pandas."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# +

data = {
    'Duration': [60, 60, 60, 45, 45, 60, 60, 450, 30, 60, 60, 60, 60, 60, 60, 60, 60, 60, 45, 60, 45, 60, 45, 60, 45, 60, 60, 60, 60, 60, 60, 60],
    'Date': ['2020/12/01', '2020/12/02', '2020/12/03', '2020/12/04', '2020/12/05', '2020/12/06', '2020/12/07', '2020/12/08', '2020/12/09', '2020/12/10',
             '2020/12/11', '2020/12/12', '2020/12/12', '2020/12/13', '2020/12/14', '2020/12/15', '2020/12/16', '2020/12/17', '2020/12/18', '2020/12/19',
             '2020/12/20', '2020/12/21', np.nan, '2020/12/23', '2020/12/24', '2020/12/25', 20201226, '2020/12/27', '2020/12/28', '2020/12/29',
             '2020/12/30', '2020/12/31'],
    'Pulse': [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 100, 106, 104, 98, 98, 100, 90, 103, 97, 108, 100, 130, 105, 102, 100, 92, 103, 100, 102, 92],
    'Maxpulse': [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 120, 120, 128, 132, 123, 120, 120, 112, 123, 125, 131, 119, 101, 132, 126, 120, 118, 132, 132, 129, 115],
    'Calories': [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0, 329.3, 250.7, 250.7, 345.3, 379.3, 275.0, 215.2, 300.0, np.nan, 323.0,
                 243.0, 364.2, 282.0, 300.0, 246.0, 334.5, 250.0, 241.0, np.nan, 280.0, 380.3, 243.0]
}


df = pd.DataFrame(data)

df

# -

# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
#
#
# # Replacing Values
#
# 1) replace the wrong value with max 'possible' value

# for x in df.index:
#
#   if df.loc[x, "Duration"] > 120:
#
#       df.loc[x, "Duration"] = 120
#     
# Вот это я нашел на https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_data.asp, жестко против такого протестую, тем более там все примеры задач решаются таким образом

df[df['Duration'] > 120] = 120
df

# # Removing Rows
#
# Another way of handling wrong data is to remove the rows that contains wrong data.
#
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.

df2 = df[df['Duration'] < 120]
df2

# # Pandas - Removing Duplicates
#
# df.duplicated() - returns True for every row if there is a duplicate

df2.duplicated()

df3 = df2.drop_duplicates() # removing duplicates
df3

# # Pandas - Data Correlations
#
# **Finding Relationships**
#
# A great aspect of the Pandas module is the corr() method.
#
# The corr() method calculates the relationship between each column in your data set.
#
# Note: The corr() method ignores "not numeric" columns, this is why we should drop such columns
#
# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
#
# The number varies from -1 to 1.
#
# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
#
# 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
#
# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
#
# 0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.
#
# What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.
#
#

df3 = df3.drop(columns='Date')
df3.corr()

#

# **Perfect Correlation:**
#
# We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relationship with itself.
#
# **Good Correlation:**
#
# "Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.
#
# **Bad Correlation:**
#
# "Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.
#
# # Pandas - Plotting
#
# Pandas uses the plot() method to create diagrams.
#
# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
#

# +
df3.plot()

plt.show()
# -

# **Scatter Plot**

df3

# +
df3.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

# +
df3.plot(kind = 'scatter', x = 'Pulse', y = 'Calories')

plt.show()

# -

# # Histogram

df3['Pulse'].plot(kind='hist')

#
