# 꺾인 부분의 개수//2 부분에 위치한 곳 부터 뒤집으면 최소
# 꺾인 부분의 개수가 늘어날 때마다 일정한 규칙이 있다
# 부분 등차수열

dummy = input()
cnt = 0

pre = dummy[0]

# 바로 이전것과 비교하여 꺾이는 부분의 개수를 추출
for i in range(1, len(dummy)):
    if pre != dummy[i]:
        cnt += 1
    pre = dummy[i]

mok = cnt % 2 == 0 and cnt // 2 or cnt // 2 + 1

if cnt <= 0:
    print("0")
else:
    print(int(mok))
