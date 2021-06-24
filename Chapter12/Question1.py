n = int(input())
size = len(n) // 2

num1 = n[:size]
num2 = n[size:]

sum1 = 0
sum2 = 0
for i in range(size):
    sum1 += int(num1[i:i+1])
    sum2 += int(num2[i:i+1])

if sum1 == sum2 :
    print('LUCKY')
else:
    print('READY')