#Pandas :Loading Data
#pandas:working with and saving data
#import pandas as pd

#Data loading
import pandas as pd
df = pd.real_csv('your_file.csv')

#what is a series?
import pandas as pd
#create a series from a list
data = [10,20,30,40,50]
s = pd.Series(data)
print(s)

#inspecting and exploring data

# Summary statistics for numerical columns
df.describe()

# Get DataFrame dimensions (rows, columns)
df.shape

# Get list of column names
df.columns

# Get unique values in a specific column
df["Column_Name"].unique()

#selecting and indexing data

# Select a single column (returns a Series)
col = df["Column_Name"]

# Select multiple columns (returns a DataFrame)
subset = df[["Col1", "Col2"]]

#Label-Based Selection (.loc) vs Index-Based Selection (.iloc)

# .loc uses labels/names
# Syntax: df.loc[row_label, column_label]
df.loc[0:3, "Col1":"Col3"]

# .iloc uses integer indices (0-indexed, exclusive of end index)
# Syntax: df.iloc[row_index, column_index]
df.iloc[0:4, 0:3]

#Filtering Data
# Filter rows based on a condition
high_val = df[df["Value"] > 50]

# Multiple conditions (& for AND, | for OR)
filtered = df[(df["Value"] > 50) & (df["Category"] == "A")]

#Modifying & Saving Data

# Add a new column
df["New_Col"] = df["Col1"] * 2

# Drop a column
df = df.drop(columns=["Unwanted_Col"])

# Save modified DataFrame to a new CSV (index=False prevents adding row numbers)
df.to_csv("updated_data.csv", index=False)

