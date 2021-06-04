# BOJ_8320
# pypy3
# 1등!!

n = int(input())

cnt = 0
for i in range(1, n+1):
    if i * i > n:
        break
    cnt += ((n//i) - (i-1))

print(cnt)



# 시간초과

# list = []
# for i in range(1, (n + 1)//2):
#
#     for j in range(1, n + 1):
#         if i * j <= n:
#             if ([j, i] in list):
#                 continue
#             list.append([i, j])
#
# print(len(list))
