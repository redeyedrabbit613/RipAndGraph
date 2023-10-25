import pandas as pd

data = pd.read_excel('testdata.xlsx')
selected_columns = data[['age', 'Name']]
print("Selected Columns:")
print(selected_columns)

selected_rows = data.loc[[0, 5, 13]]
print("Selected Rows:")
print(selected_rows)
