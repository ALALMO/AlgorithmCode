n, m = map(int, input().split())
result = 0

for i in range(n):
    data = map(int, input().split()) # 한 줄씩 입력받아 확인
    minValue = 10001
    for j in data:
        minValue = min(minValue, j) # 현재 줄에서 '가장 작은 수' 찾기
    result = max(result, minValue) # '가장 작은 수'들 중에서 가장 큰 수 찾기

print(result)