n, m, k = map(int, input().split()) # N, M, K를 공백으로 구분하여 입력받기
data = list(map(int, input().split())) # N개의 수를 공백으로 구분하여 입력받기

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
first = data[n - 2] # 두 번째로 큰 수

count = (int)(m / (k + 1)) * k
count += m % (k + 1)

result = first * count # 가장 큰 수 더하기
result += second * (m - count) # 두 번째로 큰 수 더하기

print(result)