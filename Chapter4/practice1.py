# 왕실의 나이트
point = input()
x = int(point[1])
y = ord(point[0]) - ord('a') + 1 #+1이 들어가야함
count = 0

# 2개씩 왼쪽, 오른쪽, 위, 아래 순
types = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]


for type in types:
    next_x = x + type[0]
    next_y = y + type[1]
    if 1 <= next_x <= 8 and 1 <= next_y <= 8:
        count += 1

print(count)