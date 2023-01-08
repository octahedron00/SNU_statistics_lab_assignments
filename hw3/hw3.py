import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.stats import uniform, binom, norm, chi2
from statsmodels.graphics.gofplots import ProbPlot


# 1
ames = pd.read_csv("../data/ames.csv")
sale_price = ames.loc[:, "SalePrice"]
df_sp = pd.DataFrame(sale_price)
plt.hist(sale_price, bins=20)
plt.show()
print(sale_price.describe())

'''
count      2930.000000
mean     180796.060068
std       79886.692357
min       12789.000000
25%      129500.000000
50%      160000.000000
75%      213500.000000
max      755000.000000
Name: SalePrice, dtype: float64

'''

# 2
sp50 = np.random.choice(sale_price, size=50)
print(sp50)
mean50 = np.mean(sp50)
print(mean50)

'''
[156000 161000 109008 149900 210000  60000 148000 139500 277000 119900
 115000 105900 248500 170000 161000 308030 248000 119500 136900 168165
 201000 135000 355000 175000 137000 591587 149000 213000 155000 356383
 183000 105000 111500 255900 136000 148000 112000 186000 194000 144000
 160000 205950 191000 165000 172785 197000  95000 164000 175000 143000]
180468.16

'''

# 3
sp50s = [np.random.choice(sale_price, size=50) for _ in range(5000)]
mean50s = pd.DataFrame([np.mean(sp50) for sp50 in sp50s])
plt.hist(mean50s, bins=20)
plt.show()

'''

'''

# 4
print(mean50s.describe())
print("total std : ", df_sp.std())
print("sample mean(50) std : ", mean50s.std())

'''
                   0
count    5000.000000
mean   180780.665844
std     11323.130501
min    147555.280000
25%    173129.820000
50%    180310.510000
75%    188235.105000
max    224174.700000
total std :  SalePrice    79886.692357
dtype: float64
sample mean(50) std :  0    11323.130501
dtype: float64

'''

# 5
sp150s = [np.random.choice(sale_price, size=150) for _ in range(5000)]
mean150s = pd.DataFrame([np.mean(sp150) for sp150 in sp150s])
plt.hist(mean150s, bins=20)
plt.show()
print(mean150s.describe())
print("total std : ", df_sp.std())
print("sample mean(150) std : ", mean150s.std())

'''
                   0
count    5000.000000
mean   180703.436719
std      6555.407927
min    158851.906667
25%    176239.723333
50%    180590.800000
75%    185022.968333
max    203858.833333
total std :  SalePrice    79886.692357
dtype: float64
sample mean(150) std :  0    6555.407927
dtype: float64

'''

# appendix 1
body_dims = pd.read_csv("../data/bodydims.csv")
label = {
    0: "Female",
    1: "Male"
}
body_dims["sex"] = body_dims["sex"].map(label)
print(body_dims.describe(include="object"))
print("\n")
bd_sex = body_dims["sex"]
print(bd_sex.value_counts())

'''
           sex
count      507
unique       2
top     Female
freq       260


Female    260
Male      247
Name: sex, dtype: int64

'''

# appendix 2
label_show = {
    "wgt": ["mean", "min", "max"],
    "hgt": ["mean", "min", "max"]
}
print(body_dims.groupby("sex").agg(label_show))

'''
              wgt                      hgt              
             mean   min    max        mean    min    max
sex                                                     
Female  60.600385  42.0  105.2  164.872308  147.2  182.9
Male    78.144534  53.9  116.4  177.745344  157.2  198.1

'''

# appendix 3
body_dims_M = body_dims[body_dims["sex"] == "Male"]
body_dims_F = body_dims[body_dims["sex"] == "Female"]

bdm_elb_di = body_dims_M["elb.di"]
print(bdm_elb_di.describe())
plt.hist(body_dims_M.loc[:, "elb.di"], bins=50)

y = np.linspace(bdm_elb_di.min(), bdm_elb_di.max(), 50, endpoint=True)
fy1 = norm.pdf(y, loc=[bdm_elb_di.mean()], scale=[bdm_elb_di.std()])
fy = [i*len(bdm_elb_di)/sum(fy1) for i in fy1]
plt.plot(y, fy, linewidth=1.0, linestyle="-")

plt.show()

'''
count    247.000000
mean      14.457085
std        0.882543
min       12.400000
25%       13.800000
50%       14.400000
75%       15.100000
max       16.700000
Name: elb.di, dtype: float64

'''

# appendix 4
rate = 0.383
n = 96
p = np.zeros((100, 100), dtype="longdouble")
p[0, 0] = 1
for i in range(n):
    for j in range(i+1):
        p[i+1][j] += p[i][j] * (1-rate)
        p[i+1][j+1] += p[i][j] * rate
print("From calculation : ", sum(p[n, 36:70]))

print("From ND approximation : ",
      norm.cdf(69, n*rate, math.sqrt(n*rate*(1-rate)))
      - norm.cdf(36, n*rate, math.sqrt(n*rate*(1-rate))))

print("From continuity correction : ",
      norm.cdf(69.5, n*rate, math.sqrt(n*rate*(1-rate)))
      - norm.cdf(35.5, n*rate, math.sqrt(n*rate*(1-rate))))

'''
From calculation :  0.6019265761771341
From ND approximation :  0.5640493966657784
From ND approximation :  0.6049653429802357

'''
