import pandas as pd

df = pd.read_csv(r"C:\Users\Admin\Desktop\IAUL6\Machine learning\LABS\2\house_prices.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows of the Dataset:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nData Types of Each Column:")
print(df.dtypes)



