import pandas as pd 

red_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', delimiter=';')

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
print(red_wine.columns)
red_wine.info()


red_wine['quality_label'] = red_wine['quality'].apply(lambda value: 'low'
if value <= 5 else 'medium'
if value <= 7 else 'high')


red_wine['quality_label'] = pd.Categorical(red_wine['quality_label'],
categories=['low', 'medium', 'high'])

white_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', delimiter=';')

white_wine_missing = white_wine.isna().all()

shape_1 = white_wine.shape

missing_columns = white_wine.isna().all(axis=0)

missing_rows = white_wine.isna().all(axis=1)

print(white_wine.head(5))
print(white_wine.tail(5))
print(shape_1)
print(white_wine_missing)
print(missing_columns)
print(missing_rows)
white_wine.info()

white_wine['quality_label'] = white_wine['quality'].apply(lambda value: 'low'
if value <= 5 else 'medium'
if value <= 7 else 'high')

white_wine['quality_label'] = pd.Categorical(white_wine['quality_label'],
categories=['low', 'medium', 'high'])


both_wines = pd.concat([red_wine.describe(), white_wine.describe()], axis=1, keys=["Red Wines Stats", "White Wines Stats"])

print(both_wines)




