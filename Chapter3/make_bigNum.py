def solution(number, k):
    collected = []

    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0: # 원소가 있고 맨 마지막이 숫자보다 작으면 pop
            collected.pop()
            k -= 1

        if k == 0: # 더 뺄 수 있는 것이 없으므로 나머지를 다 넣는다
            collected += number[i:]
            break

        collected.append(num)

   # if k > 0: 이거랑 밑에거랑 같은 문법
    # collected = collected[:-k]

    collected = collected[:-k] if k > 0 else collected

    answer = "".join(collected)
    return answer