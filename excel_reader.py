import pandas as pd

data = pd.read_excel('example.xlsx')

#Select specific columns by name
selected_columns = data[['Column1', 'Column2']]

#Select a specific column using the dot notation
selected_columns = data.Column1

#Select rows by their index (row number)
selected_rows = data.loc[[0, 1, 3]]

#Select rows based on a condition. selecting rows from the DataFrame 'data' where the values in 'Column1' are greater than 50.
selected_rows = data[data['Column1'] > 50]

#Combine column and row selection
selected_data = data.loc[data['Column1'] > 50, ['Column1', 'Column2']]

print("Selected Columns:")
print(selected_columns)

print("\nSelected Rows:")
print(selected_rows)

print("\nCombined Selection:")
print(selected_data)


print(data.head())
