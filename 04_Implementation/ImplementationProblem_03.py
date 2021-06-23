# 문자열 압축
# 오류 테스트 케이스-자리수

def solution(s):
    answer = len(s)

    for n in range(1, len(s)):
        sum = 1
        nsum = len(s)
        word = s[0:n]

        for i in range(n, len(s), n):
            if word == s[i:i + n]:
                sum += 1
            else:
                if sum > 1:
                    nsum -= (n * (sum - 1) - len(str(sum)))
                    sum = 1
                word = s[i:i + n]

        if sum > 1:
            nsum -= (n * (sum - 1) - len(str(sum)))

        if answer > nsum:
            answer = nsum

    return answer


print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
