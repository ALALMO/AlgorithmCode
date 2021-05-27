from itertools import combinations

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
num_count_list = []

for i in range(1, m+1):
    num_count_list.append(num_list.count(i)-1) # 자신과 중복되는 경우의수

c_list_num = len(list(combinations(num_list, 2))) # 전체 nC2의 개수를 구함


for i in num_count_list:
    if i > 0:
        c_list_num -= i #중복이 있는경우 전체 개수에서 제거

print(c_list_num)