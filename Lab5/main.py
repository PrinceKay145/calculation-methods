# метод Рунге-кутта
# variant 20(might change)
from math import exp

A = 0
B = 1
yy0 = 1.0
N = 32
H = (B - A) / N
X = [round(A + (H * i), 4) for i in range(N + 1)]
Y = [round(exp(pow(X[i], 4)), 4) for i in range(N + 1)]


# to find y using method of Runge-kutta
# for alpha=1/2
def runge0_5(x, n, h, y0):
    y = [y0]
    for i in range(n):
        y.append(
            round(
                y[i] + (h / 2*(
                    f(x[i], y[i]) + f(
                        x[i] + h, (y[i] + h * f(x[i], y[i]))
                    )
                )),
                4)
        )
    return y


##for the first derivates of y
def f(xx, yy):
    res = 4 * pow(xx, 3) * yy
    return res


y_runge_0_5 = runge0_5(X, N, H, yy0)

delta = [round(abs(y_runge_0_5[i] - Y[i]),3) for i in range(N+1)]

print("alpha = 0.5")
for i in range(N+1):
    print(f"x={X[i]}\t\t y_euler = {y_runge_0_5[i]}\t\t y={Y[i]}\t\t delta = {delta[i]}")
