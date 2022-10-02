
from math import sin, pow, sqrt

def divided_differences(x_values, y_values, k):
    result = 0
    for j in range(k + 1):
        mul = 1
        for i in range(k + 1):
            if i != j:
                mul *= x_values[j] - x_values[i]
        result += y_values[j] / mul
    return result


def create_Newton_polynomial(x_values, y_values):
    div_diff = []
    for i in range(1, len(x_values)):
        div_diff.append(divided_differences(x_values, y_values, i))

    def newton_polynomial(x):
        result = y_values[0]
        for k in range(1, len(y_values)):
            mul = 1
            for j in range(k):
                mul *= (x - x_values[j])
            result += div_diff[k - 1] * mul
        return result

    return newton_polynomial


N = 10
x0 = -1
x10 = 1
x_values = [round(x0 + (0.2 * i), 1) for i in range(N + 1)]
y_values = [round((pow(x_values[i], 2) + 2) + sin(sqrt(pow(x_values[i], 2) + 2)), 4) for i in range(N + 1)]

new_pol = create_Newton_polynomial(x_values, y_values)

M = 3*N
mx_values = [round(x0 + (0.068 * i), 1) for i in range(M + 1)]
my_values = [(pow(mx_values[i], 2) + 2) + sin(sqrt(pow(mx_values[i], 2) + 2)) for i in range(M + 1)]
#print(my_values)
mnew_pol = [new_pol(mx_values[i]) for i in range (M+1)]
delta = [abs(mnew_pol[i]-my_values[i]) for i in range(M+1)]
for i in range (M):
    print(f'x= {mx_values[i]:.4f}, \t y= {my_values[i]:.4f}, \t P={mnew_pol[i]:.4f} \t delta = {delta[i]:.2f}')
