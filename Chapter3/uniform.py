def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    intersec = set(reserve).intersection(set(lost))
    reserve = list(set(reserve).difference(intersec))
    lost = list(set(lost).difference(intersec))

    answer = n - len(lost)

    for i in lost:
        if i - 1 in reserve:
            answer += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            answer += 1
            reserve.remove(i + 1)

    return answer