import itertools


# Make List
def numList(word):
    wordList = list(word)
    permList = []
    for i in range(1, len(word) + 1):
        permList += list((itertools.permutations(wordList, i)))

    setList = []
    for i in range(len(permList)):
        setList.append(int(''.join(permList[i])))
    setList = set(setList)
    return setList


# 소수 검출
def isPrime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False

        return True


def solution(numbers):
    answer = 0
    for i in numList(numbers):
        if isPrime(i):
            answer += 1
    return answer
