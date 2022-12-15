# from scipy.stats import truncnorm

# def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
#     return truncnorm(
#         (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
# speed_input=open('speed_input.txt', 'w+')
# X = get_truncated_normal(mean=8, sd=2, low=1, upp=10)
# print(X.rvs(100), file=speed_input)

# x_ordinate=open('x_ordinate.txt', 'w+')
# Y = get_truncated_normal(mean=100, sd=2, low=0, upp=200)
# print(Y.rvs(100), file=x_ordinate)

# y_ordinate=open('y_ordinate.txt', 'w+')
# Z = get_truncated_normal(mean=100, sd=2, low=0, upp=200)
# print(Z.rvs(100), file=y_ordinate)

# from random import randrange
# print(randrange(10))

import random
import numpy as np
speed_input=open('speed_input.txt', 'w+')
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
        print(random.randint(start,end),file=speed_input)
    return res
Rand(1, 10, 500)
speed_input.close()

x_ordinate=open('x_ordinate.txt', 'w+')
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
        print(random.randint(start, end),file=x_ordinate)
    return res
Rand(0, 350, 500)
x_ordinate.close()

y_ordinate=open('y_ordinate.txt', 'w+')
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
        print(random.randint(start, end),file=y_ordinate)
    return res
Rand(0, 350, 500)
y_ordinate.close()