s = input()
s += '2'
res1 = 0
res2 = 0
char = s[0]

for i in range(1, len(s)):

    if i != len(s) and char == s[0] and char != s[i]: # 첫 글자와 같은애들의 반복
        char = s[i]
        res1 += 1

    if i != len(s) and char != s[0] and char != s[i]: # 첫 글자와 다른 애들의 반복
        char = s[i]
        res2 += 1


print(min(res1,res2))