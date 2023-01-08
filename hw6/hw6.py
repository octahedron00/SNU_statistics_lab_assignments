import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.stats import uniform, binom, norm, chi2, chisquare, chi2_contingency, ttest_rel, ttest_1samp, ttest_ind, f
from statsmodels.graphics.gofplots import ProbPlot
import seaborn as sns


# 1
x = np.array([[288, 10, 61], [378, 7, 62]])

table = pd.DataFrame(x, ["Male", "Female"], ["Know", "Not well", "Don't know"])

result = chi2_contingency(table)
chi, p, df, exp = result
print("chi2 = ", chi)
print("p value = ", p)
print("degree of freedom = ", df)
print("expected value = ")
print(exp)

'''
chi2 =  3.1290636322789274
p value =  0.2091859277257003
degree of freedom =  2
expected value = 
[[296.6426799   7.5719603  54.7853598]
 [369.3573201   9.4280397  68.2146402]]

'''


# 2
x = np.array([[11, 39], [14, 26]])

table = pd.DataFrame(x, ["Blood thinner", "none"], ["Survive", "Dead"])

result = chi2_contingency(table)
chi, p, df, exp = result
print("chi2 = ", chi)
print("p value = ", p)
print("degree of freedom = ", df)
print("expected value = ")
print(exp)

'''
chi2 =  1.2800769230769231
p value =  0.25788473323931277
degree of freedom =  1
expected value = 
[[13.88888889 36.11111111]
 [11.11111111 28.88888889]]

'''


# add 1
x = [17, 33, 35, 25]
y = [0.2, 0.3, 0.3, 0.2]
exp = [i*sum(x) for i in y]

result = chisquare(x, exp)
print(result)

'''
Power_divergenceResult(statistic=1.666666666666667, pvalue=0.6443698056370251)

'''


# add 2
x = np.array([[37, 30, 33], [35, 25, 40]])

table = pd.DataFrame(x, ["20s", "30s"], ["0 time", "1 time", "2 times"])

result = chi2_contingency(table)
chi, p, df, exp = result
print("chi2 = ", chi)
print("p value = ", p)
print("degree of freedom = ", df)
print("expected value = ")
print(exp)

'''
chi2 =  1.1813338868133387
p value =  0.5539577030655446
degree of freedom =  2
expected value = 
[[36.  27.5 36.5]
 [36.  27.5 36.5]]

'''


# add 3
x = np.array([[38, 62], [57, 43]])

table = pd.DataFrame(x, ["20s", "30s"], ["Samsung", "Apple"])

result = chi2_contingency(table)
chi, p, df, exp = result
print("chi2 = ", chi)
print("p value = ", p)
print("degree of freedom = ", df)
print("expected value = ")
print(exp)

'''
chi2 =  6.496240601503759
p value =  0.010810283451958084
degree of freedom =  1
expected value = 
[[47.5 52.5]
 [47.5 52.5]]

'''