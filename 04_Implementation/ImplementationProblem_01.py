# 럭키 스트레이트
# 2021.06.22

num = input()

def checkLucky(num):
    for i in range(len(num)):
        left = 0
        right = 0

        for j in range(len(num)):
            if j <= i:
                left += int(num[j])
            else:
                right += int(num[j])
        if left == right:
            return True
    return False


if checkLucky(num):
    print("LUCKY")
else:
    print("READY")