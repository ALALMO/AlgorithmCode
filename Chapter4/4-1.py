# 지도에서 원하는 입력을 받아 그만큼 움직이고 좌표 출력 (y,x)형태

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(moves_type)):
        if plan == moves_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx, ny

print(x,y)