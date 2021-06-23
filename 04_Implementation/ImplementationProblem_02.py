# 문자열 재정렬

strList = list(input())
strList.sort()
sum = 0
result = ""

for i in strList:
    if i.isdigit():
        sum += int(i)
        continue
    result += i

result += str(sum)
print(result)