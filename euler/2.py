i, j = 1, 2
total = 0

while j < int(4e6):
    if not j % 2:
        total += j
    i, j = j, i + j

print(total)
