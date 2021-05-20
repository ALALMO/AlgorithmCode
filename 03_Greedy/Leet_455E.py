# LeetCode_455
# Easy
# 2021.05.21
# Greedy Algorithm

class Solution(object):
    def findContentChildren(self, g, s):
        cnt = 0
        j = 0
        g.sort(reverse=True)
        s.sort(reverse=True)

        if len(s) == 0:
            return 0

        for i in range(len(g)):
            if g[i] <= s[j]:
                cnt += 1
                i += 1
                if j == len(s)-1:
                    break
                j += 1
            else:
                i += 1

        return cnt

sol = Solution()
print(sol.findContentChildren([1,2,3],[3]))