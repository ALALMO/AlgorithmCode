n = int(input())
num_list = list(map(int, input().split()))
count = 0

num_list.sort()
num_list.reverse() # num을 거꾸로 정렬

while(True):
    num_list = num_list[num_list[0]:] # 제일 큰 숫자만큼 배열을 자름 ex)맨앞이 3이면 인덱스 0,1,2를 자름
    count += 1

    if len(num_list) <= 1: # list가 1이하이면 탈출 1개가 남았을땐 마지막 그룹에 그 한명을 넣으면 되기때문
        if len(num_list) == 1 and num_list[0] == 1:#1개 남았을때만, 0개일땐 반복문 그냥 탈출
            count += 1
        break

print(count)

