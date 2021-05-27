n, m = map(int, input().split())
data = list(map(int, input().split()))
result = n * (n-1) // 2

for i in range(1, m+1):
    count = data.count(i)
    if count > 1:
        result -= count * (count - 1) // 2

print(result)