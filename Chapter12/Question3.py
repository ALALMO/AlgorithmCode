s = input()
answer = ""
min = len(s)

l = list(s)
for i in range(len(s)//2, 0, -1):
    division = [s[j:j+i] for j in range(0, len(s), i)]

    repeat = 0
    text = division[0]
    for j in division:
        if text == j:
            repeat += 1
        else:
            answer = answer + str(repeat) + text
            repeat = 1
            text = j

    answer = answer + str(repeat) + text
    answer = answer.replace("1", "")

    if len(answer) < min:
        min = len(answer)

    answer = ""

print(min)