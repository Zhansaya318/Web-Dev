def power(a, n):
    r = 1
    for i in range(n):
        r *= a
    return r

a, n = input().split()
a = float(a)
n = int(n)

print(power(a, n))