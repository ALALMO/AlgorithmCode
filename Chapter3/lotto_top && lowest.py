def rank(correct_num):
    ranking = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    return ranking[correct_num]

def solution(lottos, win_nums):
    count = 0
    lowest_rank = 0
    top_rank = 0

    for num in win_nums:
        if num in lottos:
            count += 1

    lowest_rank = rank(count)

    top_rank = rank(lottos.count(0) + count)

    answer = [top_rank,lowest_rank]
    return answer


print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
