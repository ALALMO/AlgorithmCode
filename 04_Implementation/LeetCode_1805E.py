# LeetCode_1805
# Easy
# 2020.06.03
# error test case) 167278959591294

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        list = []
        subList = []

        tmp = ""

        print(word)
        # 모두 숫자일 경우 end point
        word += 'e'

        for i in range(len(word)):
            if not (ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z')):
                tmp += word[i]
            else:
                if not tmp == "":
                    try:
                        list.append(int(tmp))

                    # int -> Stirng이 실패했을 경우
                    except:
                        subList.append(tmp)
                    tmp = ""

        intListSet = set(list)
        subListSet = set(subList)
        return len(intListSet) + len(subListSet)


print(Solution.numDifferentIntegers("a123bc34d8ef34"))
