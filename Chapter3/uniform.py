def solution (n,lost,reserve):

    lost_1 = sorted(lost)
    reserve_1 = sorted(reserve)

    for i in reserve: #체육복을 가져왔는데 잃어버린 애들 제거
        if(i in lost):
            reserve_1.remove(i)
            lost_1.remove(i)

    for i in reserve_1: # 가져온 친구 -1 부터 하는 이유  lost=[1,3,5], resere=[2,4,6]일때 i+1부터하면 3,5만 제거되고 1이남아버림
        if(i-1 in lost_1):
            lost_1.remove(i-1)
        elif(i+1 in lost_1):
            lost_1.remove(i+1)

    return n - len(lost_1)


