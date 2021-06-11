n, m, k = map(int, input().split()) #map : 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

answer = (first * k + second) * (int)(m / (k + 1))
if(m % (k + 1) != 0):
    answer += (m % (k + 1)) * first

print(answer)