import statistics
from statistics import mean as m, variance as v
# from statistics import *

example_list = [2,3,3,4,6,8,8,8,4,6,9,12,5,7]

# x = statistics.mean(example_list)
# x = mean(example_list)
x = m(example_list)

print(x)

x = statistics.median(example_list)

print(x)

x = statistics.stdev(example_list)

print(x)

x = statistics.mode(example_list)

print(x)

# x = statistics.variance(example_list)
x = v(example_list)

print(x)