n = 2000000
p = [True for i in range(n)]

i = 2
while (j := i ** 2) < n:
    if p[j]:
        for k in range(j, n, i):
            p[k] = False
    i += 1

print(sum((i for i in range(2, n) if p[i])))
