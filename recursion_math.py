def pow(x, y):
    if y <= 1:
        return x
    else:
        return x * pow(x, y - 1)


def factorial(x):
    if x <= 0:
        return 1
    else:
        return x * factorial(x - 1)

powEx = pow(2, 3)
facEx = factorial(5)

print('Factorial example: 5! =', facEx)
print('Power example 2^3 =', powEx)

