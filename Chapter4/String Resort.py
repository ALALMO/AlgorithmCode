import re

def solution(s):
    numlist = map(int, re.findall('\d', s))
    s = re.sub('\d','',s)
    num = sum(numlist)
    s = sorted(s)
    s += str(num)

    return ''.join(s)
if __name__ == "__main__":
    print(solution(input()))