# 0 또는 1일때만 +

numbers = input()
result = int(numbers[0])

for i in range(1, len(numbers)):
    if numbers[i] == 0 or numbers[i] == 1 or result == 1 or result == 0:
        result += int(numbers[i])
    else:
        result *= int(numbers[i])

print(result)