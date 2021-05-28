# 내림차순으로 정렬
# 가장 큰 공포도를 가진 그룹부터 묶으면 최대 그룹 수 검출 가능

N = map(int, input().split())

members = list(map(int, input().split()))
members.sort(reverse=True)

cnt = 0
while True:
    try:
        start = members[0]
        members = members[start:]
        cnt += 1
    except:
        break

print(cnt)

