n = input()
a = map(int, input().split())

enter = []
quit = []

point = 0
for i in a:
    point = max(point, i) + 1
    while point in enter or point in quit:
        point += 1

    c = len(quit)
    for j in quit:
        if j < point:
            c -= 1
    if c >= 5:
        point = quit[-1] + 1

    enter.append(point)
    quit.append(point + 6)

print(quit[-1])
