import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.stats import uniform, binom, norm, chi2, ttest_rel, ttest_1samp, ttest_ind, f
from statsmodels.graphics.gofplots import ProbPlot
import seaborn as sns

# 1

textbooks = pd.read_csv("./data/textbooks.txt", sep=" ")

price = textbooks[["uclaNew", "amazNew"]]
print(price.describe())
result = ttest_rel(price["uclaNew"], price["amazNew"])
print(result)

'''
          uclaNew     amazNew
count   73.000000   73.000000
mean    72.221918   59.460274
std     59.659128   48.995571
min     10.500000    8.600000
25%     24.700000   20.210000
50%     43.560000   34.950000
75%    116.000000   88.090000
max    214.500000  176.000000
Ttest_relResult(statistic=7.648771112479753, pvalue=6.927581126065491e-11)

'''

# 2
run10sample = pd.read_csv("./data/run10samp.txt", sep=" ")

print(run10sample.describe(include="all"))

'''
             time         age
count  100.000000  100.000000
mean    95.614600   35.050000
std     15.776914    8.972883
min     55.310000   20.000000
25%     85.925000   29.000000
50%     95.460000   32.500000
75%    103.995000   38.250000
max    141.940000   67.000000

'''

# add 1

male = run10sample[run10sample["gender"] == "M"]
male = male["time"]
female = run10sample[run10sample["gender"] == "F"]
female = female["time"]
gender_run = pd.DataFrame({'male_time': male, "female_time": female})
print(gender_run.describe())
sns.boxplot(data=run10sample, x="gender", y="time")
plt.show()

result = ttest_ind(male, female)
print(result)

'''
        male_time  female_time
count   45.000000    55.000000
mean    87.645333   102.134909
std     12.532218    15.236103
min     55.310000    70.120000
25%     77.860000    94.105000
50%     88.310000   101.320000
75%     97.340000   108.705000
max    114.060000   141.940000

'''

# add 2

by_state = run10sample.groupby(["state"])
by_state = by_state['time']
print(by_state.describe())

'''
       count        mean        std  ...      50%       75%     max
state                                ...                           
DC      26.0   96.321923  16.419822  ...   96.715  106.4725  128.51
IN       1.0  141.940000        NaN  ...  141.940  141.9400  141.94
LA       1.0  117.020000        NaN  ...  117.020  117.0200  117.02
MD      18.0   90.436667  18.105047  ...   88.025  101.0075  132.14
ME       1.0   96.390000        NaN  ...   96.390   96.3900   96.39
MI       1.0   97.970000        NaN  ...   97.970   97.9700   97.97
NC       1.0   68.460000        NaN  ...   68.460   68.4600   68.46
NJ       4.0   98.947500  22.919945  ...   92.690  102.8525  131.84
NY       6.0   98.190000  15.657488  ...   98.065  104.8000  120.19
PA       2.0   93.765000   9.411591  ...   93.765   97.0925  100.42
VA      39.0   95.768974  12.034769  ...   97.340  102.5550  131.99

[11 rows x 8 columns]

'''

# add 3
DC_time = run10sample[run10sample['state'] == 'DC']['time']
MD_time = run10sample[run10sample['state'] == 'MD']['time']

DC_N = DC_time.count() - 1
MD_N = MD_time.count() - 1

DC_S = float(DC_time.var()) / DC_N
MD_S = float(MD_time.var()) / MD_N

F = DC_S / MD_S

print(2 * min(f.cdf(F, dfn=DC_N, dfd=MD_N), 1 - f.cdf(F, dfn=DC_N, dfd=MD_N)))

'''
0.18195542549788948

'''


# add 4
def add(a: int, b: int):
    ans = 0
    for i in range(a, b + 1):
        ans += i
    return ans


print(add(1, 10))

'''
55

'''
