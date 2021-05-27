n = 1260
money = [500, 100, 50, 10]
count = 0

for coin in money:
    count += n / coin
    n %= coin

print(count)
