import heapq

t = int(input()) # 테스트 케이스 개수
for i in range(t):
    n = int(input()) # 지원자의 숫자
    ranking = []
    for j in range(n):
        document, interview = map(int, input().split())
        heapq.heappush(ranking, (document, interview))

    ranking.sort()

    tmp = len(ranking) + 1
    result = 0
    for k in ranking:
        document, interview = k
        if interview < tmp:
            result += 1
            tmp = interview

    print(result)