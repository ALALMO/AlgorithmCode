s = input().replace("0", "")
result = int(s[:1])

for i in range(1, len(s)):
    if int(s[i:i+1]) == 1:
        result += int(s[i:i+1])
    else:
        result *= int(s[i:i+1])

print(result)