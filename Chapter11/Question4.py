n = int(input())
data = list(map(int, input().split()))
money = {0}

data.sort()
for i in data:
    tmp = list(money)
    for j in tmp:
        money.add(i + j)
        if len(money) in money:
            print(len(money) - 1)
            break