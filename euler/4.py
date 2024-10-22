n = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        p = i * j
        s = str(p)
        m = len(s) // 2
        if s[:m] == s[m:][::-1]:
            if p > n:
                n = p

print(n)
