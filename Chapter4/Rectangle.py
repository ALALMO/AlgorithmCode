n = int(input())
count = n
for i in range(2, n//2):
    j = i
    while True:
        if i * j <= n:
            count += 1
            j += 1
        else:
            break;

print(count)
