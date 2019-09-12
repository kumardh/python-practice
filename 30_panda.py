import pandas as pd

# Example 1: Creating a dataframe using List:
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
df = pd.DataFrame(lst)
print(df)

# Example 2: Creating a dataframe using Dict:
lst = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
df = pd.DataFrame(lst)
print(df)

# Example 3: Creating a dataframe using xlsx:
file = 'students.xlsx'
xl = pd.ExcelFile(file)
print(xl.sheet_names)
pd.read_excel()
print(xl.sheet_names[0])
df = pd.read_excel('students.xlsx', 'Sheet1',index_col ='Student');
print(df);
print(type(df));

# Example 4: Read dictionary use some useful method and save to excel file.
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
df = pd.DataFrame(dict)
print(df.loc[2: , ["country","capital"]])
print(df.sum())
print(df.sort_values(by="country"))
df.to_excel('population.xlsx',  sheet_name='Sheet1')

# Example 5: Assign named idex to DataFrame
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
brics = pd.DataFrame(dict)
print(brics)
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]
# Print out brics with new index values
print(brics)

# Example 6: Select two columns
print(df[['School', 'Standard']])

# Example 7: Retrieving row by loc and iloc
first = df.loc['Manav']
print(first)
third = df.iloc[2]
print(third)

# Example 8: Filling missing value using fillna()
df1 = df.fillna(0)
print(df1)

# Example 9: Using dropna() function
df2 = df.dropna()
print(df2)

# Example 10: iterating over rows using iterrows() function
for i, j in df.iterrows():
    print(i, j)
    print()

# Example 11: creating a list of dataframe columns
columns = list(df)

for i in columns:
       # printing the third element of the column
       print(df[i][2])

