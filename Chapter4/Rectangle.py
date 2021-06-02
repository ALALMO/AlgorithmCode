n = int(input())
result = 1 # (1*1)

for i in range(2, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    result += (count + 1) // 2

print(result)