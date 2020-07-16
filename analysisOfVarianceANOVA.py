# The independent t-test is used to compare the means of a condition between 2 groups. ANOVA is used when one wants
# to compare the means of a condition between 2+ groups.

import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

dfData = pd.read_csv("E:/PycharmProjects/statisticalAnalysis/difficile.csv")
dfData.drop('person', axis=1, inplace=True)
dfData['dose'].replace({1: 'placebo', 2: 'low', 3: 'high'}, inplace=True)
print(rp.summary_cont(dfData['libido']))

print("========================")
# To perform an ANOVA test there are a few ways this can be done with Python.
print(stats.f_oneway(dfData['libido'][dfData['dose'] == 'high'],
                     dfData['libido'][dfData['dose'] == 'low'],
                     dfData['libido'][dfData['dose'] == 'placebo']))
aov_table = sm.stats.anova_lm(result, typ=2)
print(aov_table)