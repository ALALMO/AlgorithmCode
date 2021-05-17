n, k= map(int, input().split())
result = 0

while True:
    #한번에 빼기
    target = (n // k) * k #n을 k배수로 만듬
    result += (n - target) # 배수 만들때까지 뺀것들
    n = target
    if n<k:
        break
    n //= k
    result += 1

result += (n-1) # result에 결과값인 1빼고 남은 만큼 더함(사실상 빼는 횟수)
print(result)