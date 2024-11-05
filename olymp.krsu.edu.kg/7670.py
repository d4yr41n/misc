n, m, k = map(int, input().split())
a = sorted(map(int, input().split()))

c = 0
i = 0
while i < n:
    x = a[i]
    j = i + 1
    l = 1
    while j < n and a[j] - x <= m and l < k:
        j += 1
        l += 1
    c += 1
    i = j
print(c)
