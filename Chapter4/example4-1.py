from copy import copy

n = int(input())
data = input().split()
result = [1, 1]
move = [1, 1]

for i in data:
    move = copy(result)

    if i == "L":
        move[1] -= 1
    elif i == "R":
        move[1] += 1
    elif i == "U":
        move[0] -= 1
    elif i == "D":
        move[0] += 1

    if move[0] != 0 and move[1] != 0:
        result = move

print(result)