import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("Crime.csv")

# Task 1
avg_cr_now = np.average(df["CrimeRate"])
avg_cr_then = np.average(df["CrimeRate10"])
msg = "\n # Завдання 1\n"\
    f"Середня частота злочинів зараз: {avg_cr_now}\n"\
    f"Середня частота злочинів 10 років тому: {avg_cr_then}"
print(msg)

# Task 2
print("\n# Завдання 2")
# Спосіб 1 - порівняння вибірки із випадковою вибіркою
np.random.seed(1)
h0_now = np.random.normal(np.mean(df["CrimeRate"]), np.std(df["CrimeRate"]), len(df))
h1_now = df["CrimeRate"]
result_now = stats.ttest_ind(h0_now, h1_now)    # Порівняння мат. сподівань двох вибірок
if result_now.pvalue > 0.005:
    print(f"П-значення для першого експерименту є більшим за 0.005, а саме: {result_now.pvalue}\n"\
            "CrimeRate нормально розподілена вибірка")
else:
    print(f"П-значення для першого експерименту є меншим за 0.005, а саме: {result_now.pvalue}\n"\
            "CrimeRate не є нормально розподіленою вибіркою")

# Спосіб 2 - використання готової функції scipy.stats.normaltest()
h1_then = df["CrimeRate10"]
result_then = stats.normaltest(h1_then)
if result_then.pvalue > 0.05:
    print(f"П-значення для другого експерименту є більшим за 0.05, а саме: {result_then.pvalue}\n"\
            "CrimeRate10 нормально розподілена вибірка")
else:
    print(f"П-значення для другого експерименту є меншим за 0.005, а саме: {result_then.pvalue}\n"\
            "CrimeRate10 не є нормально розподіленою вибіркою")

# Task 3
print("\n# Завдання 3")
if np.mean(df["CrimeRate"]) < np.mean(df["CrimeRate10"]):
    alt = "less"
else:
    alt = "greater"
result = stats.ttest_rel(df["CrimeRate"], df["CrimeRate10"], alternative=alt)
if result.pvalue > 0.05:
    print("За останні 10 років частота злочинів практично не змінилась")
else:
    if alt == "less":
        print("За останні 10 років частота злочинів зменшилась")
    else:
        print("За останні 10 років частота злочинів зросла")

# Task 4
print("\n# Завдання 4")
rel_now = stats.spearmanr(df["CrimeRate"], df["Wage"])
if rel_now.pvalue > 0.05:
    print(f"Жодного зв'язку між CrimeRate та Wage нема. П-значення = {rel_now.pvalue}")
else:
    print(f"Зв'язок між CrimeRate та Wage є. Його сила = {rel_now.correlation}")

rel_then = stats.spearmanr(df["CrimeRate10"], df["Wage10"])
if rel_then.pvalue > 0.05:
    print(f"Жодного зв'язку між CrimeRate10 та Wage10 нема. П-значення = {rel_then.pvalue}")
else:
    print(f"Зв'язок між CrimeRate10 та Wage10 є. Його сила = {rel_then.correlation}")