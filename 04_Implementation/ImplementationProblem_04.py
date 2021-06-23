# 자물쇠와 열쇠
# 다시!

def solution(key, lock):
    rotate_key = key

    for i in range(4):
        tmpLock = lock
        rotate_key = rotateArr(rotate_key)
        arr = sumArr(tmpLock, rotate_key)
        if check_Key(arr):
            return True
    return False


def check_Key(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < 1:
                return False
    return True


def sumArr(A, B):
    sum = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return sum


def rotateArr(arr):
    n = len(arr)
    m = len(arr[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = arr[i][j]
    return result


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))