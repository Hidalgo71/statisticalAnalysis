# The paired sample t-test is also called dependent sample t-test. It’s a univariate test that tests for a significant difference between 2 related variables.
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
bpData = pd.read_csv("E:/PycharmProjects/statisticalAnalysis/blood_pressure.csv")
print(bpData[['bp_before', 'bp_after']].describe())

bpData[['bp_before', 'bp_after']].plot(kind='box')

plt.savefig('boxplot_outliers.png')
# plt.show()

