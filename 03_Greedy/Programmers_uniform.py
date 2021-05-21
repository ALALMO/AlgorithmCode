def solution(n, lost, reserve):
    answer = 0
    i = 0
    j = 0

    lost.sort()
    reserve.sort()

    lost, reserve = removeDuple(lost,reserve)
    print(lost, reserve)
    cnt = len(lost)




    while i < len(lost) and j < len(reserve):
        if lost[i] < reserve[j]:
            if checkLost(lost[i], reserve[j]) == 1 or checkLost(lost[i], reserve[j]) == 2:
                cnt -= 1
                i += 1
                j += 1
            else:
                i += 1

        else:
            if checkLost(reserve[j], lost[i]) == 1 or checkLost(reserve[j], lost[i]) == 2:
                cnt -= 1
                i += 1
                j += 1
            else:
                j += 1
    answer = n - cnt
    return answer


def checkLost(l, r):
    if l + 1 == r:
        return 1
    elif l - 1 == r:
        return 2
    else:
        return -1

def removeDuple(lost, reserve):
    i = 0
    j = 0
    while i < len(lost) and j < len(reserve):
        if (lost[i] == reserve[j]):
            lost.pop(i)
            reserve.pop(j)
        elif (lost[i] > reserve[j]):
            j = j + 1
        else:
            i = i + 1

    return lost, reserve

print(solution(5,[1,2,3],[2,3,4]))
