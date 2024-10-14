import pandas as pd

red_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv')

missing_values_df = red_wine.isna().any()


missing_values_columns = red_wine.isna().any(axis=0)


missing_values_rows = red_wine.isna().any(axis=1)

shape = red_wine.shape

print(red_wine.head(5))
print(red_wine.tail(5))
print(shape)
print(missing_values_columns)
print(missing_values_df)
print(missing_values_rows)
red_wine.info()

# we are creating a new column called "quality_label", we define a range and associate that range with a label
red_wine['quality_label'] = red_wine["quality"].apply(lambda value: 'low'
if value <= 5 else 'medium'
if value <= 7 else 'high')

# here we are transforming these labels into categrical data type (specific to pandas) instead of simple string
red_wine['quality_label'] = pd.Categorical(red_wine['quality_label'],
categories=['low', 'medium', 'high'])




