import itertools
import math

# 제곱근까지만 보고 소수를 판별하는 함수
def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
    # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    redundant = [] # 숫자 중복을 계산을 줄이기 위한 리스트
    for i in range(1, len(numbers)+1): # permutation을 1개 ~ number의 갯수까지 순열계산
        a = list(itertools.permutations(list(numbers), i)) # a에 i개의 순열 계산 리스트를 집어 넣음
        for k in range(len(a)):
            b = a[k] # a의 리스트중(조합 중) 0번째부터 a의 끝가지
            result = 0 # list를 숫자로 합치기 위함
            for i in b: # 리스트를 숫자로 합치기
                result *= 10
                result += int(i)

            if(redundant.count(result) != 0): # 중복되는 숫자가 있다면 continue
                continue
            else: # 중복 되는 숫자가 없으면 redundant에 넣고 소수인지 판별
                redundant.append(result)
                if(is_prime_number(result)): # 소수이면 answer 1증가
                    answer += 1
    return answer

if __name__ == "__main__" :
    print(solution("011"))
