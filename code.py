# Importing pandas library
import pandas as pd

# Sample datasets
data1 = {'ID': [1, 2, 3, 4],
         'Name': ['Alice', 'Bob', 'Charlie', 'David']}
data2 = {'ID': [1, 2, 5, 6],
         'Age': [25, 30, 35, 40]}

# Creating DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Indexing - selecting specific rows and columns
# Selecting specific row by index
row_2_df1 = df1.loc[1]  # Selecting the row with index label 1
print("Row 2 from df1:\n", row_2_df1)

# Selecting specific column
name_column_df1 = df1['Name']  # Selecting the 'Name' column
print("\nName column from df1:\n", name_column_df1)

# Slicing - selecting specific ranges of rows and columns
# Selecting multiple rows
rows_2_to_3_df1 = df1.loc[1:2]  # Selecting rows with index labels from 1 to 2
print("\nRows 2 to 3 from df1:\n", rows_2_to_3_df1)

# Selecting specific range of columns
subset_df2 = df2[['ID', 'Age']]  # Selecting only 'ID' and 'Age' columns
print("\nSubset of df2:\n", subset_df2)

# Merging - combining datasets based on common columns
merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Merging based on 'ID' column
print("\nMerged DataFrame:\n", merged_df)
