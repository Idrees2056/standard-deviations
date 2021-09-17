from numpy import square
from numpy.core.fromnumeric import std
import pandas as pd
import statistics
import math

df = pd.read_csv("data.csv")
data = df["Marks"].tolist()

#first step
mean=statistics.mean(data)

#step two
deviations = []
for g in data:
    o=g-mean
    deviations.append(o)
print(deviations)
#step three
square_deviations=[]
for d in deviations:
    k=d*d
    square_deviations.append(k)

#step four
sum_squared_deviations=0
for k in  square_deviations:
    sum_squared_deviations=sum_squared_deviations+k
print(sum_squared_deviations)
#step five
variance=sum_squared_deviations/30
print(variance)
#step six
std=math.sqrt(variance)
print(std)