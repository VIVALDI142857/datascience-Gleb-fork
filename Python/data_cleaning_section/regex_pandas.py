"""Regular expressions using pandas."""

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

data = {'samples': ('conect us at joinfuturebuilders@yahoo.com', 
                  'send us your summary at jobhit@gmail.com',
                  'plase email alicetourism@mail.ru',
                  'Reach out to support@example.com if you need assistance.',
                  'you are always most welcome at +8985436456')}
df = pd.DataFrame(data)

df

pattern = r'[\w\.-]+@[\w\.-]+'
df['result'] = df['samples'].apply(lambda x: re.findall(pattern, x))

df

data1 = {'raw_text': ['Product ID: 123-XYZ',
                     'Product ID: 456-ABC',
                     'Product ID: -',
                     'Product ID: 789-PQR']}
df1 = pd.DataFrame(data1)
df1

pattern1 = r'Product ID: (\d+-\w+)'
df1['product_id'] = df1['raw_text'].apply(lambda x: 
    re.search(pattern1, x).group(1) 
    if re.search(pattern1, x) else None)
df1

# # HOW TO USE REGEX IN PANDAS
# https://kanoki.org/2019/11/12/how-to-use-regex-in-pandas/

# https://drive.google.com/file/d/1RqYIwbReNOgLVvxjsQgHieMyZFiJ3na5/view?usp=share_link

d_ = '/Users/glebtrofimov/Downloads/world-happiness-report-2019.csv'
df2 = pd.read_csv(d_)
df2

df2['first_five_letter'] = df2['Country (region)'].str.extract(r'(^\w{5})')
df2

# # Pandas Count

r_=pd.Series(['Finland','Colombia','Florida','Japan','Puerto Rico','Russia','france'])
r_[r_.str.count(r'(^F.*)')==1]

# For practice i decided to count countries that start with each letter and compare the results

# +
s_ = df2['Country (region)']

x_: list[str] =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l_: list[int] = []

for i_ in x_:
    l_.append(len(s_[s_.str.count(fr'(^{i_}\w*)') == 1]))

df3 = pd.DataFrame({'first_letters': x_, 'count': l_})
df3.plot('first_letters', 'count', kind='bar')
plt.ylabel('counts')
plt.xlabel('first letters')
plt.show()
# -

# # Pandas match
#
# match () function is equivalent to python’s re.match() and returns a boolean value. We are finding all the countries in pandas series starting with character ‘P’ (Upper case) .

r_[r_.str.match(r'(^P.*)')==True]

df2[df2['Country (region)'].str.match('^P.*') == True]

# # Pandas Replace

w_= pd.Series(['Finland-1','Colombia-2','Florida-3','Japan-4','Puerto Rico-5','Russia-6','france-7'])
w_.replace(r'(-\d)','',regex=True, inplace = True)
w_

# # Pandas Findall

r_= pd.Series(['Finland','Colombia','Florida','Japan','Puerto Rico','Russia','france'])
r_.str.findall('^[Ff].*')

# # Pandas Contains

r_.str.contains(r'^F\.*')

# # Pandas Split

f_ = pd.Series(["StatueofLiberty built-on 28-Oct-1886"])
f_.str.split(r"\s", n=-1,expand=True)

# # Replace values in Pandas dataframe using regex
# https://www.geeksforgeeks.org/replace-values-in-pandas-dataframe-using-regex/

# +
df4 = pd.DataFrame({'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
					'Cost':[10000, 5000, 15000, 2000, 12000]})

index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
		pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]

df4.index = index_

df4

# -

df4.replace(to_replace=r'[Nn]ew\s', value='New_', regex=True)

# +
df5 = pd.DataFrame({'City':['New York (City)', 'Parague', 'New Delhi (Delhi)', 'Venice', 'new Orleans'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
					'Cost':[10000, 5000, 15000, 2000, 12000]})


index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
		pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]

df5.index = index_

df5


# +
# Function to clean the names
def Clean_names(City_name):
    # Search for opening bracket in the name followed by
    # any characters repeated any number of times
    if re.search(r'\(.*', City_name):
 
        # Extract the position of beginning of pattern
        pos = re.search(r'\(.*', City_name).start()
 
        # return the cleaned name
        return City_name[:pos]
 
    else:
        # if clean up needed return the same name
        return City_name
         
# Updated the city columns
df5['City'] = df5['City'].apply(Clean_names)
 
# Print the updated dataframe
df5
# -

#
