import pandas as pd
import numpy as np

import Coloring as c

df = pd.read_csv("Crime.csv")

# task 1
# Виділення однієї колонки
task1_a = df["CrimeRate"]
print("\n # Завдання 1\n")
c.fancyPrint("Виділення однієї колонки: \n" + str(task1_a.head()), [c.Colors.fg.green])
c.fancyPrint("Тип даних: " + str(type(task1_a)), [c.Colors.fg.green], end="\n\n")
# Підмасив
task1_b = task1_a[:10]
c.fancyPrint("Підмасив: \n" + str(task1_b), [c.Colors.fg.red], end="\n\n")
# Задання назв індексів
task1_c = task1_b.rename(lambda x: x*2)
c.fancyPrint("Задання назв індексів: \n" + str(task1_c.head()), [c.Colors.fg.green], end="\n\n")
# Непряма індексація
task1_d1 = task1_a.loc[task1_a >= np.mean(task1_a)]
c.fancyPrint("Непряма індексація: \n" + str(task1_d1), [c.Colors.fg.red], end="\n\n")
# Пряма індексація
task1_d2 = task1_a.iloc[::5]
c.fancyPrint("Пряма індексація: \n" + str(task1_d2), [c.Colors.fg.green], end="\n\n")


# task 2
print("\n # Завдання 2\n")
# Додавання колонки
df["DeltaCR"] = df["CrimeRate"] - df["CrimeRate10"]
c.fancyPrint("Додавання колонки: \n" + str(df["DeltaCR"][::5]), [c.Colors.fg.red], end="\n\n")
# Додавання рядка (№100)
tmp = {}
for col in df.columns:
    tmp[col] = np.mean(df[col])
tmp = pd.DataFrame(data=tmp, index=[100])
df = pd.concat([df, tmp])
c.fancyPrint("Додавання рядка (№100): \n" + str(df[-5:]), [c.Colors.fg.green], end="\n\n")
# Видалення рядка (№100)
df.drop(index=100, inplace=True)
c.fancyPrint("Видалення рядка (№100): \n" + str(df[-5:]), [c.Colors.fg.red], end="\n\n")
# Видалення колонки (DeltaCR)
df.drop("DeltaCR", axis=1, inplace=True)
c.fancyPrint("Видалення колонки (DeltaCR): \n" + str(df[-5:]), [c.Colors.fg.green], end="\n\n")


# task 3
print("\n # Завдання 3\n")
# Підставлення колонки на місце індексу
tmp = df.copy(deep=True)
tmp = tmp.set_index("CrimeRate")
c.fancyPrint("Підставлення колонки на місце індексу: \n" + str(tmp.head(3)), [c.Colors.fg.red], end="\n\n")
# Статистичний опис колонок
tmp = df.describe()
c.fancyPrint("Статистичний опис колонок: \n" + str(tmp), [c.Colors.fg.green], end="\n\n")
# Типи даних колонок
tmp = df.dtypes
c.fancyPrint("Типи даних колонок: \n" + str(tmp), [c.Colors.fg.red], end="\n\n")
# Зміни типу даних колонки
c.fancyPrint(f"CrimeRate datatype before: {df['CrimeRate'].dtype}", [c.Colors.fg.green])
tmp = df.astype({'CrimeRate': str}, errors='ignore')
c.fancyPrint(f"CrimeRate datatype after: {tmp['CrimeRate'].dtype}", [c.Colors.fg.green], end="\n\n")
# Групування значень + агрегуюча функція
tmp = df.groupby("Southern").first()    # Зчитує перше not NULL значення
c.fancyPrint("Групування значень ('Youth') + first(): \n" + str(tmp), [c.Colors.fg.red], end="\n\n")
# Агрегуюча функція
tmp = df.groupby("Southern").count()    # Рахує not NULL значення
c.fancyPrint("Приклад використання агрегуючої функції count(): \n" + str(tmp), [c.Colors.fg.green], end="\n\n")
# Підмасив за ознаками
tmp = df[(df['Education'] >= np.mean(df["Education"])) & df['Southern'].isin([0])]
c.fancyPrint("Створення підмасиву за ознаками: \n" + str(tmp.head()), [c.Colors.fg.red], end="\n\n")


# task 4
print("\n # Завдання 4\n")
# pd.concat()
youth = df["YouthUnemployment"]
mature = df["MatureUnemployment"]
unemployment = pd.concat([youth,mature], axis=1)
c.fancyPrint("Приклад використання pd.concat(): \n" + str(unemployment.head()), [c.Colors.fg.green], end="\n\n")
# pd.merge()
wage = df[["Wage","Southern"]]
below_wage = df[["BelowWage","Southern"]]
wages = pd.merge(wage, below_wage, left_on="Southern", right_on="Southern")
c.fancyPrint("Приклад використання pd.merge(): \n" + str(wages.head()), [c.Colors.fg.red], end="\n\n")