import pandas as pd

file_path = "/Users/yizou/Use Python/Just_test/Name.csv"
data = pd.read_csv(file_path)

print(data.head())
#print(data.tail())
#print(data.info())
#print(data.describe())
print(data.describe()["Age"])
print(data.columns)
print(data.isnull())
print(data.isnull().sum())
age = data['Age']
print(f"age is :{age}")
age_name = data[['Age', 'Age', 'Date','Score']]
print(age_name)
print(data.iloc[4:5, :])

print(data[(data['Age'] > 40) & (data['Score']<90)])
print(data[(data['Age'] > 40) & (data['Date'].notnull())])
print(data[(data['Age'] > 40) | (data['Score'] <90)])


selected_data = data[["Age","Score", "Name", "Date"]]
print(selected_data)

sorted_data = selected_data.sort_values(by='Age')
#print(sorted_data)
#clean_data = sorted_data.dropna()
#print(sorted_data.dropna())

sorted_data['Age'] = sorted_data['Age'].fillna(sorted_data['Age'].max())
print(sorted_data)

# create
sorted_data['age/score'] = sorted_data["Age"] / sorted_data['Score']
print(sorted_data)
sorted_data = sorted_data.dropna()
print(sorted_data)
data1 = pd.DataFrame({'Age':[12, 100], 'Score': [66, 100]})
sorted_data = pd.concat((sorted_data, data1))
print(sorted_data)

import matplotlib.pyplot as plt

sorted_data['Age'].plot(kind='hist', title="Age")
plt.show(block=False)
plt.pause(2)
plt.close()

plt.figure(figsize=(8, 6))
plt.plot(sorted_data['Age'], sorted_data['Score'], marker='o')
plt.xlabel('Age')
plt.show(block=False)
plt.pause(2)
plt.close()

sorted_data.plot(x='Age', y='Score', kind='line', title="chart2",)
plt.show(block=False)
plt.pause(2)
plt.close()

sorted_data.to_csv('output.csv', index=False)