# 00시 00분 00초 부터 N시 59분 59초까지 3이 포함된 시각의 경우의 수 모두 구하기
# 데이터 100만개 이상일땐 완전 탐색

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1

print(count)