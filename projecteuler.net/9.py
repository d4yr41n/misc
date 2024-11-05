# a^2 + b^2 = c^2
# a + b + c = 1000

# c = 1000 - a - b | ^2
# c^2 = 1000^2 - 2000a - 2000b + a^2 + b^2 + 2ab | c^2 -> a^2 + b^2
# a^2 + b^2 = 1000^2 - 2000a - 2000b + a^2 + b^2 + 2ab
# 0 = 1000^2 - 2000a - 2000b + 2ab | /2
# 0 = 500000 - 1000a - 1000b + ab
# 1000a + 1000b - ab = 500000 | /1000
# a + b - ab / 1000 = 500

for i in range(1, 999):
    for j in range(1, 999):
        if i + j - i * j // 1000 == 500:
            print(i * j * (1000 - i - j))
            break 
    else:
        continue
    break
