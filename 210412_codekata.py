def complex_number_multiply(a, b):
    a = a.split('+')
    b = b.split('+')
    a[1] = a[1][:-1]
    b[1] = b[1][:-1]

    a, b = list(map(int, a)), list(map(int, b))

    y = str(a[0] * b[1] + a[1] * b[0]) + 'i'
    x = str(a[0] * b[0] + -(a[1] * b[1]))

    return f'{x}+{y}'

print(complex_number_multiply("1+3i", "1+-2i"))