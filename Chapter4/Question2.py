n, m = map(int, input().split()) # n:세로 크기, m:가로 크기
x, y, direction = map(int, input().split()) # (a,b):캐릭터의 좌표, d:바라보는 방향(0:북, 1:동, 2:남, 3:서)
map = [list(map(int, input().split())) for _ in range(n)] # 0:육지, 1:바다

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장 (1:방문)
d[x][y] = 1 # 현재 좌표
dx = [-1, 0, 1, 0] # 북, 남 방향 정의
dy = [0, 1, 0, -1] # 동, 서 방향 정의

result = 1
turn_time = 0

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and map[nx][ny] == 0: # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        d[nx][ny] = 1
        x = nx
        y = ny
        result += 1
        turn_time = 0
        continue
    else: # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        turn_time += 1

    if turn_time == 4: # 네 방향 모두 갈 수 없는 경우
        nx = x - dx[direction]
        ny = y - dy[direction]

        if map[nx][ny] == 0: # 뒤로 갈 수 있다면 이동
            x = nx
            y = ny
        else: # 뒤가 바다로 막혀있는 경우
            break
        turn_time = 0

print(result)