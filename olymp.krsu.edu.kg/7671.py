n, m = map(int, input().split())
h = tuple(map(int, input().split()))

mx = 1
d = {}

for i in range(n - 1):
    diff = abs(h[i] - h[i + 1])
    if diff:
        if diff in d:
            d[diff] += 1
        else:
            d[diff] = 1
        if diff > mx:
            mx = diff

s = sum(d.values()) + 1
for i in range(1, mx + 1):
    s -= d.get(i, 0)
    if s == m:
        print(i)
        break
    elif s < m:
        print(-1)
        break
