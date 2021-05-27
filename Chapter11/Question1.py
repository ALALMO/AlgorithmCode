n = int(input())
data = list(map(int, input().split()))
count = 0
result = 0

data.sort()
for i in data:
    count += 1
    if i == count:
        result += 1
        count = 0

print(result)