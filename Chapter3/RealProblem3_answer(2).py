n, k = map(int, input().split())
result = 0

while True: # (N == K로 나누어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k: # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        break

    result += 1
    n //= k

result += (n - 1)
print(result)