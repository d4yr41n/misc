n = 1
i = 2

while i <= 10001:
    n += 2
    for j in range(2, int(n ** .5) + 1):
        if not n % j:
            break
    else:
        i += 1

print(n)
