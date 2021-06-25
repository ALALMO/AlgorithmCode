def solution(s):
    length = (len(s) // 2) + 1 # 절반만 비교해보면됌
    min = len(s) # 최소값을 현재 s길이로 초기화

    for i in range(1, length): # 1 ~ s길이 절반만큼 토막 자르기
        result = ''
        s2 = s # 줄여나갈 문자열
        s3  = s[0:i] # i만큼 자른 앞 문자
        s2 = s2[i:] # s3문자만큼 s2에서 문자 빼주기
        num = 1
        while len(s2) >= 1:# s2를 쭈욱 돔
            if s3 == s2[0:i]: # s2에서 i만큼 자른 문자가 같은지 비교 같으면 num++
                num += 1
                s2 = s2[i:]
            else: # 다르면 s3에 현재 s2의 i만큼 자른 값을 넣고 s2를 i만큼 자른 값을 빼줌
                if num == 1: # 1이면 글자만
                    result += s3
                else:
                    result += str(num) + s3 # 숫자 + 글자를 집어 넣어줌
                num = 1
                s3 = s2[0:i]
                s2 = s2[i:]

        if num == 1: # 1이면 글자만
            result += s3
        else:
            result += str(num) + s3  # 숫자 + 글자를 집어 넣어줌
        print(result)
        if min > len(result):
            min = len(result)

    return min

if __name__ == '__main__':
    print(solution(input()))