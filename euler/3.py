N = 600851475143
n = 2

for i in range(3, int(N ** .5) + 1, 2):
    if not N % i:
        for j in range(2, int(i ** .5) + 1):
            if not i % j:
                break
        else:
            n = i

print(n)
