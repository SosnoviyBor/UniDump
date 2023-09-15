import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


from scipy import stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def count_entries(dist, intervals):
    interval_size = (dist.max() - dist.min()) / intervals
    entries_list = []
    limit_left = dist.min()

    for _ in range(0, intervals):
        limit_right = limit_left + interval_size
        counter = 0
        for n in dist:
            if limit_left <= n < limit_right:
                counter += 1
        entries_list.append([[limit_left, limit_right], counter])
        limit_left = limit_right
    return entries_list


def get_limit_list(entries, intervals):
    return [[entries[i][0][0], entries[i][0][1]]
            for i in range(intervals)]


def chi2(perfect_dist, observed_dist, intervals, len):
    chi2 = 0
    for i in range(intervals):
        expected = len * perfect_dist[i]
        chi2 += pow(observed_dist[i] - expected, 2) / expected
    return chi2


def observed_expected_chi2(expected_list, observed_list, intervals, len):
    observed_chi2 = chi2(expected_list, observed_list, intervals, len)
    expected_chi2= stats.chi2.ppf(1-.05, intervals - 1)
    return observed_chi2, expected_chi2


def plot_histogram(intervals, arr):
    df = pd.DataFrame(arr, columns=['Value'])
    sns.histplot(df, bins=intervals, x="Value", kde=True)
    plt.show()