import statistics as stats
import pandas as pd

import generators.utils as utils

class GeneratorBase:
    def __init__(self, amount, intervals):
        self.amount = amount
        self.intervals = intervals
        
        self.generated_dist = self._gen_dist()

        self.average = stats.mean(self.generated_dist)
        self.dispersion = stats.pvariance(self.generated_dist)

        self.entries = utils.count_entries(self.generated_dist, self.intervals)
        self.limit_list = utils.get_limit_list(self.entries, self.intervals)

        self.perfect_dist = self._gen_perfect_dist()

    def _get_stats(self):
        entry_count = [i[1] for i in self.entries]
        observed_chi_2, expected_chi_2 = utils.observed_expected_chi2(
            self.perfect_dist, entry_count, self.intervals, self.amount)
        
        if observed_chi_2 < expected_chi_2:
            legit_dist_msg = "✔️  Generated distribution follows its distribution law"
        else:
            legit_dist_msg = "❌  Generated distribution DOES NOT follow its distribution law"
        
        print(
            f"{pd.DataFrame(self.entries)}\n" +
            "----------------------------------------------\n" +
            f"Average: {self.average}\n" +
            f"Dispersion: {self.dispersion}\n" +
            f"Observed chi2: {observed_chi_2}\n" +
            f"Expected chi2: {expected_chi_2}\n" +
            "----------------------------------------------\n" +
            legit_dist_msg + "\n"
        )
        
        utils.plot_histogram(self.intervals, self.generated_dist)

    def validate(self):
        pass
        # print(
        #     "\n### Task X ###\n" +
        #     ""
        # )
        # self._get_stats(self)

    def _gen_dist(self):
        pass
        # dist = []
        # for _ in range(self.amount):
        #     val = 0
        #     dist.append(val)
        # return np.array(dist)
    
    def _gen_perfect_dist(self):
        pass
        # return [0 for i in range(self.intervals)]