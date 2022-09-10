import numpy as np
import pandas as pd

def foo():
    data = pd.read_csv("iris.csv")
    col = "petal_width"
    print(f"\nData statistics for column '{col}'\n"\
            "---------\n"\
            f"Min value = {min(data[col])}\n"\
            f"Max value = {max(data[col])}\n"\
            f"Mean value = {np.mean(data[col])}\n"\
            f"Dispersion = {np.var(data[col])}\n"\
            f"Mean square error = {np.std(data[col])}\n"\
            f"Median = {np.median(data[col])}\n"\
            f"Percentile 25 = {np.percentile(data[col],25)}\n"\
            f"Percentile 75 = {np.percentile(data[col],75)}\n"
    )
    return

if __name__ == "__main__":
    foo()