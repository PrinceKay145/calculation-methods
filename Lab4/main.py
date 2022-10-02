# variant 20
# https://youtu.be/z0L_znzMfX4
import numpy as np

a = 0
b = 1
y0 = 1
n = 32
h = (b - a) / n - 1
# x_values = [round(a + (h * i), 2) for i in range(n)]
# print(x_ values)
x = np.round(np.linspace(a, b, n),4)
y = np.zeros([n])


def func(x, y, n, h):
    y[0] = y0

    for i in range(1, n):
        res = 4 * (pow((x[i - 1]), 3)) * y[i - 1]
        y[i] = y[i - 1] + (h * res)
    return y


def f(x, y):
    lis = []
    for i in range(n):
        res = round(4 * pow((x[i]), 3) * y[i],6)
        lis.append(res)
    return lis


# eur(h, n, x, y, y0)
Y_euler = np.round(func(x, y, n, h),6)
y = f(x, y)

delta = [round(abs(Y_euler[i]-y[i]),4) for i in range (n)]
print
for i in range(n):
    print(f"x= {x[i]}\t\tY_euler = {Y_euler[i]}\t\tY = {y[i]}\t\t delta= {delta[i]}")

# #print Q4
# for i in range(n):
#     if delta[i]<=0.02:
#         print(f"x= {x[i]}\t\tY_euler = {Y_euler[i]}\t\tY = {y[i]}\t\t delta= {delta[i]}")