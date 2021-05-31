n = int(input())
time = ""
result = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if time.count("3"):
                result += 1

print(result)