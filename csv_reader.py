import csv

with open('examplefile.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

#For CSV files that have a header row. 'csv.DictReader' allows you to access data by column names.  
with open('examplefile.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row['column_name']

