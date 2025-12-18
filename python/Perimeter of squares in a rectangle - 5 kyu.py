def perimeter(n):
    a, b = 1, 1
    total = a
    for i in range(n):
        a, b = b, a + b
        total += a
    return total * 4
