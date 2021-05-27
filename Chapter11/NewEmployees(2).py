t = int(input()) # 테스트 케이스 개수
for i in range(t):
    n = int(input()) # 지원자의 숫자
    ranking = [0 for j in range(n+1)]
    ranking[0] = len(ranking) + 1
    for j in range(n):
        document, interview = map(int, input().split())
        ranking[document] = interview

    result = 0
    tmp = len(ranking) + 1
    for j in ranking:
        if j < tmp:
            result += 1
            tmp = j

    print(result)