from functools import cache


@cache
def f(n):
    a = []
    for i in range(2, int(n ** .5) + 1):
        if not n % i:
            a.append(i)
            a.extend(f(n // i))
            break   
    else:
        a.append(n)
    return a


a = []

for i in range(2, 21):
    b = f(i)
    for j in b:
        if j not in a:
            a.append(j)
        else:
            for i in range(b.count(j) - a.count(j)):
                a.append(j)

n = 1
for i in a:
    n *= i
print(n)
