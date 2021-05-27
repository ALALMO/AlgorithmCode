k = int(input())
food_times = list(map(int, input().split()))
answer = 0
index = 0
q = k // len(food_times)
r = k % len(food_times)
carry = 0

for i in range(len(food_times)):
    if food_times[i] >= q + carry:
        food_times[i] -= (q + carry)
        carry = 0
    else:
        food_times[i] = 0
        carry = q + carry - food_times[i]


for i in range(r):
    if food_times[i] >= 1 + carry:
        food_times[i] -= (1 + carry)
        carry = 0
    else:
        food_times[i] = 0
        carry = 1 + carry - food_times[i]




while carry != 0:
    if food_times.count(0) == len(food_times):
        answer = -1
        break
    if food_times[r] >= 1:
        food_times[r] -= 1
        r += 1
        carry -= 1
    else:
        r += 1

while True:
    r %= len(food_times)
    if food_times[r] != 0:
        answer = r+1
        break
    else:
        r += 1

print(answer)