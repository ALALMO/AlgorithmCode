n, m = map(int, input().split())
a, b, d = map(int, input().split()) #a가 북쪽에서 떨어진칸 y라는 의미 b는 반대


minimap = list([[0] * m for i in range(n)])
#맵 정보 입력 받기
for i in range(n):
    minimap[i] = list(map(int, input().split()))

minimap[a][b] = 2 #시작 지점은 도착한것으로 처리

# 북, 동, 남, 서 방향
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

count = 1
turn_count = 0

while(True):
    #시작하자마자 방향을 돌림
    d = (3 + d) % 4

    na = a + da[d]
    nb = b + db[d]

    #0일대 이동 아니면 턴
    if minimap[na][nb] == 0:
        count += 1
        minimap[na][nb] = 2
        a = na
        b = nb
        turn_count = 0
        continue
    else:
        turn_count += 1

    #턴 카운트가 4면 뒤로갈지 나갈지 판정
    if turn_count == 4:
        na = a - da[d]
        nb = b - db[d]

        if minimap[na][nb] != 1:
            a = na
            b = nb
        else:
            break;
        turn_count = 0

print(count)