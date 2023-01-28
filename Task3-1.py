import pandas as pd 
import numpy as np

array = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
array.sort

arithmetic_mean = sum(array)/len(array)

mean_square_deviation_sum = 0
for i in array:
    mean_square_deviation_sum += (i - arithmetic_mean) ** 2
mean_square_deviation = (mean_square_deviation_sum/(len(array)-1)) ** 0.5

biased_variance = (mean_square_deviation_sum/len(array))
unbiased_variance = (mean_square_deviation_sum/(len(array)-1))

print (f'arithmetic mean = {arithmetic_mean}\nmean square deviation = {mean_square_deviation}\nbiased variance = {biased_variance}\nunbiased variance = {unbiased_variance}')
s = pd.Series([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
print(s.describe())
