import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import researchpy as rp

irData = pd.read_csv("E:\PycharmProjects\statisticalAnalysis\Iris_Data.csv")

print(irData.groupby("species")['sepal_width'].describe())

print("================================")

# To make the code a bit cleaner to read in the rest of the example, we will create 2 data frames that are subsets of
# the original data where each data frame only contains data for a respective flower species.

setosa = irData[(irData['species'] == 'Iris-setosa')]
setosa.reset_index(inplace=True)
versicolor = irData[(irData['species'] == 'Iris-versicolor')]
versicolor.reset_index(inplace=True)
# Check for homogeneity of variances.
print(stats.levene(setosa['sepal_width'], versicolor['sepal_width']))

print("================================")

diff = setosa['sepal_width'] - versicolor['sepal_width']
# check for normality visually with a p-p plot and a histogram plot.
stats.probplot(diff, plot=plt)
plt.title('sepal width P-P Plot')
plt.savefig('Sepal Width Residuals.png')
# plt.show()

print(stats.ttest_ind(setosa['sepal_width'], versicolor['sepal_width']))

print(rp.summary_cont(irData.groupby("species")['sepal_width']))

descriptives, result = rp.ttest(setosa['sepal_width'], versicolor['sepal_width'])
descriptives

print(result)