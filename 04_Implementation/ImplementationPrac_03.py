start = input()
x = int(start[1])
y = int(ord(start[0])) - int(ord('a')) + 1

moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0
for move in moves:
    if 1 <= x + move[0] <= 8 and 0 < y+move[1] < 9:
        cnt += 1

print(cnt)
