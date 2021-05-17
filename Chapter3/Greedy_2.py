n,m,k = map(int, input().split())

data = list(map(int,input().split()))

data.sort()

first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

#  3-1 데이터가 100억개 이하일 때 사용 할 수 있는 알고리즘
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#
#     if m == 0:
#         break
#
#     result += second #
#     m -= 1

#데이터가 100억개 이상일때 사용 할 수 있는 알고리즘 3-2
count = int(m/(k+1)) * k #수열이 반복 되는 횟수
count += m % (k + 1) # m이 반복되는 수열로 나누어 떨어지지 않을때 나머지를 더해줌

result = 0
result += count * first # 가장 큰 수가 나오는 획수
result += (m-count) * second # 두번째로 큰 수가 나오는 횟수

print(result)
