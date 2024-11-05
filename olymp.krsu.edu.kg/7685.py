from math import ceil, floor
from heapq import heapify, heappop, heappush


n, d = map(int, input().split())

c = {i: 0 for i in range(1, n + 1)}

for i in range(d):
    i, j = map(int, input().split())
    c[i] += 1
    c[j] += 1

v = c.values()

mx = max(v)
mn = min(v)

v = [-(mx - i) for i in v]
heapify(v)
a = heappop(v)
b = heappop(v)
while a and b:
    heappush(v, a + 1)
    heappush(v, b + 1)
    a = heappop(v)
    b = heappop(v)

if a or b:
    dist = n - 1
    diff = mx - mn - (mx * dist - d * 2) % 2

    def f(diff):
        np = n % 2
        if n < diff:
            m = ceil(diff / dist)
            nd = m - ((m * dist - diff) % 2)
            if nd:
                return m + f(nd)
            return m
        elif n > diff:
            dp = diff % 2
            if np:
                if dp:
                    return 1
                else:
                    return 2
            else:
                if dp:
                    return 0
                else:
                    return 1
        else:  
            if np:
                return 3
            else:
                return 2

    print(mx + f(diff))
else:
    print(mx)
