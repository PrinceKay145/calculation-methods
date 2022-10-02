from math import pow, sqrt, sin


# функция для нахождения Q
def create_basic_polynomial(x_values, i):
    def basic_polynomial(x):
        divider = 1  # числитель
        result = 1  # знаменатель
        for j in range(N + 1):
            if j != i:
                result *= (x - x_values[j])
                divider *= (x_values[i] - x_values[j])
        return result / divider

    return basic_polynomial


# функция для нахождения L
def create_Lagrange_polynomial(x_values, y_values):
    basic_polynomials = []  # сохраняю все Q
    for i in range(N + 1):
        basic_polynomials.append(create_basic_polynomial(x_values, i))

    def lagrange_polynomial(x):
        result = 0
        for i in range(N + 1):
            result += y_values[i] * basic_polynomials[i](x)
        return result

    return lagrange_polynomial


N = 10#заданное число
x0 = -1 #начало отрезка
x10 = 1 #конец отрезка

# задание 1
x_values = [round(x0 + (0.2 * i), 1) for i in range(N + 1)]

# задание 2
y_values = [round((pow(x_values[i], 2) + 2) + sin(sqrt(pow(x_values[i],2)+2)), 2) for i in range(N + 1)]

# задание 3
lag_pol = create_Lagrange_polynomial(x_values, y_values)

# задание 4
M = 3 * N
mx_values = [round(x0 + (0.069 * i), 4) for i in range(M + 1)]

# задание 5,6
my_values = [round((pow(mx_values[i], 2) + 2) + sin(sqrt(pow(mx_values[i],2)+2)), 2) for i in range(M + 1)]

mlag_pol = [lag_pol(mx_values[i]) for i in range(M+1)]

delta = [abs(mlag_pol[i] - my_values[i]) for i in range(M + 1)]
for i in range(M):
    if delta[i]<=0.01:
        print(f'x= {mx_values[i]:.4f}, \t y= {my_values[i]:.6f}, \t L= {mlag_pol[i]:.6f}, \t delta= {delta[i]:.2f}')
