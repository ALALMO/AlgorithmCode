s = input()

alphabet = []
sum = 0
for i in range(len(s)):
    if 0 <= ord(s[i:i+1]) - ord('0') <= 9:
        sum += ord(s[i:i+1]) - ord('0')
    else:
        alphabet.append(s[i:i+1])

alphabet.sort()
print("".join(alphabet) + str(sum))