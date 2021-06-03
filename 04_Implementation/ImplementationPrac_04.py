N, M = map(int, input().split())
x, y, dir = map(int, input().split())

wholeMap = []
for i in range(N):
    wholeMap.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

stack = []
stack.append([x,y]) # 시작점

turnTime = 0
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3


while True:
    turn_left()
    nx = x+dx[dir]
    ny = y+dy[dir]

    if not ([nx, ny] in stack) and wholeMap[nx][ny] == 0:
        stack.append([nx, ny])
        x, y = nx, ny
        turnTime = 0
        continue
    else:
        turnTime += 1

    if turnTime == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if wholeMap[nx][ny] == 0:
            x = nx
            y = ny
            if not ([nx, ny] in stack):
                stack.append([nx, ny])
        else:
            break
        turnTime = 0

print(len(stack))