import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.stats import uniform, binom, norm, chi2
from statsmodels.graphics.gofplots import ProbPlot


# 1
ames = pd.read_csv("../data/ames.csv")

living_area = ames["Gr.Liv.Area"]

print("Mean value of total : ", living_area.mean())
print("Variance of total : ", living_area.var())
'''
Mean value of total :  1499.6904436860068
Variance of total :  255539.23531322062

'''

# 2
sp60 = living_area.sample(n=60)
print("Mean value of the sample : ", sp60.mean())
'''
Mean value of the sample :  1499.75

'''

# 3
mean = living_area.mean()
std = living_area.std()/math.sqrt(60)
print(norm.ppf(0.025, mean, std), " ~ ", norm.ppf(0.975, mean, std))
'''
1371.7813972553886  ~  1627.599490116625

'''


# add 1
means = []
for _ in range(10000):
    a = norm.rvs(loc=0, scale=5, size=25)
    means.append(a.mean())
plt.hist(means, bins=np.linspace(-15, 15, num=30))

x = np.linspace(-15, 15, num=10000)
plt.plot(x, 10000*norm.pdf(x))
plt.show()
'''

'''


# add 2
samples = [177.4, 161.5, 158.3, 179.0, 174.2, 182.2, 162.6, 170.3, 162.9, 155.4,
           175.9, 174.7, 177.3, 164.5, 168.1, 162.9, 177.3, 165.4, 159.8, 159.4]
df = pd.DataFrame(samples)
print(df.mean())
print(df.std())
print(df.std()/math.sqrt(20))

mean = df.mean()
std = math.sqrt(50)/math.sqrt(20)
print(norm.ppf(0.025, mean, std), " ~ ", norm.ppf(0.975, mean, std))
'''
0    168.455
dtype: float64
0    8.167231
dtype: float64
0    1.826248
dtype: float64
[164.87561908]  ~  [172.03438092]

'''

# add 3
mean = 100
std = 30/4
print(norm.ppf(0.025, mean, std), " ~ ", norm.ppf(0.975, mean, std))
'''
85.30027011594959  ~  114.69972988405041

'''
