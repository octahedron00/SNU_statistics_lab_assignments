import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.stats import uniform, binom, norm, chi2, chisquare, chi2_contingency, ttest_rel, ttest_1samp, ttest_ind, f, \
    pearsonr, probplot
from statsmodels.graphics.gofplots import ProbPlot
from statsmodels.formula.api import ols
from statsmodels.stats.stattools import durbin_watson
import statsmodels.api as sm
import seaborn as sns


# 1

# make a dataframe
arr = {'col': [16, 19, 25, 22, 21, 15, 16, 22, 21, 18] + [13, 14, 15, 16, 15, 13, 19, 16, 20, 14, 11]
              + [18, 18, 15, 14, 14, 10, 18, 15, 15] + [11, 15, 11, 17, 17, 13, 14, 16, 13, 11],
       'num': [1 for _ in range(10)] + [2 for _ in range(11)] + [3 for _ in range(9)] + [4 for _ in range(10)]
       }
print(arr)
media = pd.DataFrame(arr)

# try anova
model = ols("num ~ C(col)", data=media).fit()
print(model.summary())
table = sm.stats.anova_lm(model, typ=2)
print(table)

# box plot of all data
media.boxplot('col', by=['num'])
plt.show()


# add 1

# make a dataframe
arr = {'col': [13, 14, 15, 16, 15, 13, 19, 16, 20, 14, 11]
              + [18, 18, 15, 14, 14, 10, 18, 15, 15] + [11, 15, 11, 17, 17, 13, 14, 16, 13, 11],
       'num': [2 for _ in range(11)] + [3 for _ in range(9)] + [4 for _ in range(10)]
       }
print(arr)
media = pd.DataFrame(arr)

# try anova
model = ols("num ~ C(col)", data=media).fit()
print(model.summary())
table = sm.stats.anova_lm(model, typ=2)
print(table)


# 2

# make a dataframe
arr = {'y': [210, 230, 190, 180, 190, 195, 170, 200, 190, 193, 295, 275, 290, 275, 265],
       'a': ["Box " + str(i) for i in range(1, 4) for _ in range(5)],
       'b': ["Shop" + str(i) for i in range(1, 6)]*3
       }
print(arr)
sell = pd.DataFrame(arr)

# try anova
model = ols("y ~ C(a) + C(b)", data=sell).fit()
print(model.summary())
table = sm.stats.anova_lm(model, typ=2)
print(table)


# add 2

# mean and std for each column
sell_ = pd.DataFrame({"Box 1": [210, 230, 190, 180, 190],
                      "Box 2": [195, 170, 200, 190, 193],
                      "Box 3": [295, 275, 290, 275, 265]})
print(sell_.describe())

# box plot of all data
sell.boxplot('y', by=['a'])
plt.show()

# try anova
model = ols("y ~ C(a)", data=sell).fit()
print(model.summary())
table = sm.stats.anova_lm(model, typ=2)
print(table)


# 3

# make a dataframe
arr = {'y': [10, 7, 9, 6, 8, 5, 4, 7, 4, 5, 5, 4, 6, 3, 2, 3, 4, 5, 1, 2],
       'a': ["Male" for _ in range(10)] + ["Female" for _ in range(10)],
       'b': (["High-protein" for _ in range(5)] + ["Low-Protein" for _ in range(5)])*2
       }
print(arr)
ability = pd.DataFrame(arr)

# try anova without considering interaction
model = ols("y ~ C(a) + C(b)", data=ability).fit()
print(model.summary())
table = sm.stats.anova_lm(model, typ=2)
print(table)


# add 3

# box plot of all data
ability.boxplot('y', by=['a', 'b'])
plt.show()

# interaction plot of all data
sns.pointplot(x='a', y='y', hue='b', data=ability)
plt.show()

# try anova with considering interaction
model = ols("y ~ C(a) * C(b)", data=ability).fit()
print(model.summary())
table = sm.stats.anova_lm(model, typ=2)
print(table)