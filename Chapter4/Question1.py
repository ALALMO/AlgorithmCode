start = input()
result = 0
x, y = ord(start[:1]) - 96, int(start[1:])
moving = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

for i in moving:
    if x + i[0] > 0 and x + i[0] < 9 and y + i[1] > 0 and y + i[1] < 9:
        result += 1

print(result)