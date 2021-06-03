N = int(input())
move = input().split()
location = [1, 1]

for i in range(len(move)):
    x, y = location[0], location[1]
    if move[i] == "L":
        y -= 1
    elif move[i] == "R":
        y += 1
    elif move[i] == "U":
        x -= 1
    else:
        x += 1

    if x < 1 or y < 1:
        continue
    location[0], location[1] = x,y

print(location)

