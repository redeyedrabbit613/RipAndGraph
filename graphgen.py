import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('testdata.xlsx')
names = data['Name']
values = data['weight']
plt.bar(names, values)
plt.xlabel('Names')
plt.ylabel('Weight')
plt.title("Test Chart")
plt.show()

