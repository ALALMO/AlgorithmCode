n = 1260
cnt = 0

coin = [500, 100, 50, 10]

for c in coin:
    cnt += n // coin
    n %= coin

print(cnt)
