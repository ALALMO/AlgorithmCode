num_list = list(map(int, list(input()))) #스트링 입력받아서 바로 리스트로 바꾸기

res = 0

for num in num_list:
    if res == 0 or num == 0 or num == 1:
        res += num
    else:
        res *= num

print(res)