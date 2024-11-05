n = int(input())
a = tuple(map(int, input().split()))


a0 = a[0]
a1 = a[0] * 2

path0 = "O"
path1 = "M"

i = 1
while i < n:
    ai = a[i]
    buf = a0 + ai * 2
    if a0 < a1:
        a0 = a1 + ai
        path0, path1 = path1 + "O", path0 + "M"
    else:
        a0 = a0 + ai
        path0, path1 = path0 + "O", path0 + "M"
    a1 = buf
    i += 1


if a0 < a1:
    print(a1)
    print(path1)
else:
    print(a0)
    print(path0)
