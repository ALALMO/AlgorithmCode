def solution(word):
    sum = 0
    redundant = []
    count = 0
    for s in word:
        if '0' <= s and s <= '9':
            sum *= 10
            sum += int(s)
        elif sum != 0 :
            if sum not in redundant:
                redundant.append(sum)
                sum = 0
                count += 1
            else:
                sum = 0

    if sum != 0:
        if sum not in redundant:
            count += 1

    return count



if __name__ == "__main__" :
    print(solution("gi851a851q8510v"))
