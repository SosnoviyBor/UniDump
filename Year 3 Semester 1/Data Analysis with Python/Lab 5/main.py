import re
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Microsoft_Stock.csv")
df = df.astype({"Date":"datetime64"})
df.set_index("Date", inplace=True)

inp = input("Виберіть опцію [0-2][A-E]\n").lower()

# task 0
if inp == "0":
    i = pd.date_range("2022-01-01", periods=12, freq="M")
    a = pd.Series([random.random() for x in range(12)], index=i)[:"2022-06-01"]
    print(a, end="\n\n")
    i = pd.date_range("2021-01-01", periods=365, freq="D")
    b = pd.Series([random.random() for x in range(365)], index=i)[:5]
    print(b)

# task 1
elif re.match("1[a-e]", inp):
    task1 = {
        "1a": df,                                   # 1А - Загальний графік зміни ціни на час відкриття біржі
        "1b": df.loc["2020-01-01":"2021-01-01"],    # 1B - Графік зміни ціни на час відкриття біржі за 2019 рік
        "1c": df.loc["2021-02-01":"2021-03-01"],    # 1C - Графік зміни ціни за січень 2021
        "1d": df.loc["2017-05-01":"2021-07-01"],    # 1D - Графік зміни ціни за травень 2017 - червень 2021
        "1e": df.loc["2019-01-01":"2021-01-01"]     # 1E - Графік зміни ціни за грудень 2019 - 2021
    }
    data = task1[inp]
    sns.lineplot(data, x=data.index, y=data["Open"]-data["Close"], hue=data.index.year)

# task 2
elif re.match("2[a-e]", inp):
    task2 = {
        "2a": df.groupby(df.index.year).mean()["Low"][2019],        # 2A - Середні значення "Low" за 2019 рік
        "2b": df.resample("M").mean(),                              # 2B - Середні значення "Low" за кожний місяць
        "2c": df["2020-06-01":"2020-12-01"].resample("2W").mean(),  # 2C - Середні значення "Low" за кожні 2 тижня літа-осені 2018
        "2d": df["2018-09-01":"2018-12-01"].pct_change()[1:],       # 2D - Зміна (у відсотках) "Low" за осінь 2018
        "2e": df["2018-01-01":"2019-01-01"].rolling(30).mean()      # 2E - Ковзне середнє з вікном у місяць (30 днів) за 2018
    }
    data = task2[inp]
    if re.match("2[a-c]", inp):
        text = {
            "2a": "Середня найнижча ціна акцій за 2019 рік: {}",
            "2b": "Середня найнижча ціна акцій за кожен місяць:\n{}",
            "2c": "Середня найнижча ціна акцій за кожні 2 неділі літа-осені 2020 (у відсотках):\n{}"
        }
        result = text[inp].format(data)
        print(result)
    else:
        sns.lineplot(data, x=data.index, y=data["Low"])

# not a task 💀
else:
    print("Wrong input!")

plt.show()