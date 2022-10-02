import scipy.integrate as integrate
from math import sin

N = 16
a = -1
b = 1
# h=(b-a)/N
# x_values=[a+i*h for i in range(N+1)]
# psi = [a+(i-1/2)*h for i in range (1, N+1)]
I = integrate.quad(lambda x: sin(2 * x + 1), a, b)


def lev_integral(f, x2, x1, n):
    delta = (x2 - x1) / n
    res = 0
    for i in range(N - 1):
        res += f(x1 + (i * delta)) * delta
    return res


def prav_integral(f, x2, x1, n):
    delta = (x2 - x1) / n
    res = 0
    for i in range(1, N):
        res += f(x1 + (i * delta)) * delta
    return res


def trapezi(f, x2, x1, n):
    delta = (x2 - x1) / n
    res = 0
    for i in range(N):
        first_val = f(x1 + i * delta)
        second_val = f(x1 + (i + 1) * delta)
        res += ((first_val + second_val) / 2) * delta
    return res


def simpson(f, x2, x1, n):
    delta = (x2 - x1) / n
    res = 0
    for i in range(N):
        first_val = f(x1 + i * delta)
        second_val = 4 * f(x1 + (i + 1 / 2) * delta)
        third_val = f(x1 + (i + 1) * delta)
        res += ((first_val + second_val + third_val) / 6) * delta
    return res


def f(x):
    return sin((2 * x) + 1)


# print(x_values)
# print(psi)

# leftInt=[lev_integral(f,x_values[i],x_values[i+1],N) for i in range(N)]
# rightInt=[prav_integral(f,x_values[i],x_values[i+1],N) for i in range(N)]
# trapezium=[trapezi(f,x_values[i],x_values[i+1],N) for i in range(N)]
# print(leftInt)
# print(rightInt)

print(
    f"N= {N}\t I= {I[0]:.4f}\tI(N,L) = {lev_integral(f, b, a, N):.4f}\t I(N,R)={prav_integral(f, b, a, N):.4f}\tI(N,T) = {trapezi(f, b, a, N):.4f}\t I(N,S) = {simpson(f, b, a, N):.4f}")
N = 2 * N
print(
    f"N= {N}\t I= {I[0]:.4f}\tI(N,L) = {lev_integral(f, b, a, N):.4f}\t I(N,R)={prav_integral(f, b, a, N):.4f}\tI(N,T) = {trapezi(f, b, a, N):.4f}\t I(N,S) = {simpson(f, b, a, N):.4f}")
N = 5 * N
print(
    f"N= {N}\t I= {I[0]:.4f}\tI(N,L) = {lev_integral(f, b, a, N):.4f}\t I(N,R)={prav_integral(f, b, a, N):.4f}\tI(N,T) = {trapezi(f, b, a, N):.4f}\t I(N,S) = {simpson(f, b, a, N):.4f}")
N = 10 * N
print(
    f"N= {N}\t I= {I[0]:.4f}\tI(N,L) = {lev_integral(f, b, a, N):.4f}\t I(N,R)={prav_integral(f, b, a, N):.4f}\tI(N,T) = {trapezi(f, b, a, N):.4f}\t I(N,S) = {simpson(f, b, a, N):.4f}")
# 3
print("-----------------------------------")
print("Задание 3")
for N in range(998, 1002):
# N=998
    print(
        f"N= {N}\t I= {I[0]:.4f}\t I(N,L) = {lev_integral(f, b, a, N):.4f}\t {abs(I[0] - lev_integral(f, b, a, N)):.3f}")

#4
print("-----------------------------------")
print("Задание 4")
for N in range(999,1003):
    print(f"N= {N}\t I= {I[0]:.4f}\tI(N,R) = {prav_integral(f, b, a, N):.4f}\t {abs(I[0] -prav_integral(f, b, a, N)):.3f}")

#5
print("-----------------------------------")
print("Задание 5")
for N in range(29,33):
    print(f"N= {N}\t I= {I[0]:.4f}\tI(N,T) = {trapezi(f, b, a, N):.4f}\t {abs(I[0] - trapezi(f, b, a, N)):.3f}")

#6
print("-----------------------------------")
print("Задание 6")
for N in range(4,11,2):
    print(f"N= {N}\t I= {I[0]:.4f}\tI(N,S) = {simpson(f, b, a, N):.4f}\t {abs(I[0] - simpson(f, b, a, N)):.3f}")
