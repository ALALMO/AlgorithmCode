def solution(n):

    n= str(n)
    sum1 = 0
    sum2 = 0
    length = len(n) // 2
    for i in range(length):
        sum1 += int(n[i])

    for i in range(length, len(n)):
        sum2 += int(n[i])

    if sum1 == sum2:
        return 'LUCKY'
    else:
        return 'READY'


if __name__ == "__main__":
    print(solution(int(input())))