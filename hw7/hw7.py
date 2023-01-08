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
import seaborn as sns


# 1

hand_span = pd.read_csv("data/handspan.txt", sep="\t")
print(hand_span.describe())

# scatter_plot
sns.relplot(x="Height", y="HandSpan", data=hand_span)
plt.show()

# correlation analysis
print("correlation analysis")
print(hand_span.corr())

# correlation analysis 2
print(pearsonr(hand_span["Height"], hand_span["HandSpan"]))

# scatter_plot with regression line
sns.lmplot(x="Height", y="HandSpan", data=hand_span)
plt.show()

# regression model print
print("regression model print")
model = ols("Height ~ HandSpan", hand_span).fit()
print(model.summary())

# regression model and residual plot
_, ax = plt.subplots()
sns.scatterplot(x=model.fittedvalues, y=model.resid_pearson)
ax.axhline(y=0)
plt.title("studentized residuals of fitted values")
plt.xlabel("fitted values")
plt.ylabel("studentized residuals")
plt.show()


# 2

car_stopping = pd.read_csv("data/carstopping.txt", sep="\t")
print(car_stopping.describe())

# scatter_plot
sns.relplot(x="Speed", y="StopDist", data=car_stopping)
plt.show()

# correlation analysis
print("correlation analysis")
print(car_stopping.corr())
print(pearsonr(car_stopping["Speed"], car_stopping["StopDist"]))

# scatter_plot with regression line
sns.lmplot(x="Speed", y="StopDist", data=car_stopping)
plt.show()

# regression model print
print("regression model print")
model = ols("Speed ~ StopDist", car_stopping).fit()
print(model.summary())

# regression model and residual plot
_, ax = plt.subplots()
sns.scatterplot(x=model.fittedvalues, y=model.resid_pearson)
ax.axhline(y=0)
plt.title("studentized residuals of fitted values")
plt.xlabel("fitted values")
plt.ylabel("studentized residuals")
plt.show()


# Sqrt value of stop_dist
car_stopping["StopDistSqrt"] = car_stopping.apply(lambda row: math.sqrt(row.StopDist), axis=1)

# scatter_plot
sns.relplot(x="Speed", y="StopDistSqrt", data=car_stopping)
plt.show()

# correlation analysis
print("correlation analysis")
print(car_stopping.corr())
print(pearsonr(car_stopping["Speed"], car_stopping["StopDistSqrt"]))

# scatter_plot with regression line
sns.lmplot(x="Speed", y="StopDistSqrt", data=car_stopping)
plt.show()

# regression model print
print("regression model print")
model = ols("Speed ~ StopDistSqrt", car_stopping).fit()
print(model.summary())

# regression model and residual plot
_, ax = plt.subplots()
sns.scatterplot(x=model.fittedvalues, y=model.resid_pearson)
ax.axhline(y=0)
plt.title("studentized residuals of fitted values")
plt.xlabel("fitted values")
plt.ylabel("studentized residuals")
plt.show()


# 3

hospital = pd.read_csv("data/hospital.txt", sep="\t")
print(hospital.describe())

hospital1 = hospital[["InfctRsk", "Stay", "Age", "Xray"]]
print(hospital1.describe())

# pair_scatter_plot
sns.pairplot(data=hospital1)
plt.show()

# correlation analysis
print("correlation analysis")
print(hospital1.corr())
print("InfctRsk, Stay", pearsonr(hospital1["InfctRsk"], hospital1["Stay"]))
print("InfctRsk, Age", pearsonr(hospital1["InfctRsk"], hospital1["Age"]))
print("InfctRsk, Xray", pearsonr(hospital1["InfctRsk"], hospital1["Xray"]))
print("Stay, Age", pearsonr(hospital1["Stay"], hospital1["Age"]))
print("Stay, Xray", pearsonr(hospital1["Stay"], hospital1["Xray"]))
print("Age, Xray", pearsonr(hospital1["Age"], hospital1["Xray"]))

# regression model print
print("regression model print")
model = ols("InfctRsk ~ Stay + Age + Xray", hospital1).fit()
print(model.summary())

# regression model and residual plot
_, ax = plt.subplots()
sns.scatterplot(x=model.fittedvalues, y=model.resid_pearson)
ax.axhline(y=0)
plt.title("studentized residuals of fitted values")
plt.xlabel("fitted values")
plt.ylabel("studentized residuals")
plt.show()


# add 1

# make a new DataFrame
hospital2 = hospital[["Xray", "Beds", "Census", "Nurses", "Facilities"]]
print(hospital2.describe())

# pair_scatter_plot
sns.pairplot(data=hospital2)
plt.show()


# add 2

# correlation analysis
print("correlation analysis")
print(hospital2[["Census", "Beds"]].corr())
print("Census, Beds", pearsonr(hospital2["Census"], hospital2["Beds"]))

# regression model print
print("regression model print")
model = ols("Beds ~ Census", hospital2).fit()
print(model.summary())

# regression model and residual plot
_, ax = plt.subplots()
sns.scatterplot(x=model.fittedvalues, y=model.resid_pearson)
ax.axhline(y=0)
plt.title("studentized residuals of fitted values")
plt.xlabel("fitted values")
plt.ylabel("studentized residuals")
plt.show()

sns.distplot(model.resid_pearson, bins=15)
plt.show()

probplot(model.resid_pearson, plot=plt)
plt.show()

print("Durbin Watson by func : ", durbin_watson(model.resid_pearson))

e = model.resid_pearson

a, b = 0, 0
for i in range(0, len(e)):
    a += e[i]*e[i]
    b += (e[i]-e[i-1])*(e[i]-e[i-1])
print("Durbin Watson by hand : ", b/a)

a, b = 0, 0
for i in range(1, len(e)):
    a += e[i]*e[i]
    b += (e[i]-e[i-1])*(e[i]-e[i-1])
print("Durbin Watson by hand : ", b/a)


# add 3

# regression model print
print("regression model print")
model = ols("Facilities ~ Xray + Beds + Census + Nurses", hospital2).fit()
print(model.summary())

# regression model print without Xray, Census (inputs whose p is over 0.05)
print("regression model print")
model = ols("Facilities ~ Beds + Nurses", hospital2).fit()
print(model.summary())


# regression model and residual plot
_, ax = plt.subplots()
sns.scatterplot(x=model.fittedvalues, y=model.resid_pearson)
ax.axhline(y=0)
plt.title("studentized residuals of fitted values")
plt.xlabel("fitted values")
plt.ylabel("studentized residuals")
plt.show()

sns.distplot(model.resid_pearson, bins=15)
plt.show()

probplot(model.resid_pearson, plot=plt)
plt.show()


print("Durbin Watson by func : ", durbin_watson(model.resid_pearson))


# TODO

