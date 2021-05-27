# 각 무게당 개수를 구한 후 그 무게를 제외한 것들의 곱의 합
# 단, 이미 진행된 무게쌍은 안되기 때문에 N-ballCnt를 이용해 제거

N, M = map(int, input().split())
balls = list(map(int, input().split()))

list = [0 for i in range(M)]


# 각 무게별 개수
for i in range(len(balls)):
    list[balls[i]-1] += 1

# 현재까지 진행된 무게의 볼
ballCnt = 0

# 총 횟수
result = 0
for i in range(len(list)):
    ballCnt += list[i]
    result += (list[i] * (N-ballCnt))

print(result)


