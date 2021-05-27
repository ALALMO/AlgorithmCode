n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

target = 1 #target은 내가 만들 수 있는 숫자보다 항상 1 큰 숫자, 처음엔 갖고있는게 없으므로 1

for num in num_list:
    if target < num: #target보다 num이 커버리면 target을 못 만든다.
        break
    target += num

print(target)

