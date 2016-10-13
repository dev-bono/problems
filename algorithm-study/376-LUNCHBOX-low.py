
def heat(list):
    """
    모든 도시락을 데우는 시간 + 한 도시락을 먹는데 걸리는 시간

    증명 :
    - 도시락의 목록이 주어질 때 먹는데 가장 오래 걸리는 샤브샤브 도시락을 제일 먼저 데우는 최적해가 반드시 하나가 있음을 보여준다
    - 먹는 시간의 역순으로 정렬하는 이유는 시간을 최소화 하기 위해서는 마지막에 도시락을 먹는데 걸리는 시간이 제일 짧아야하기 때문이다
    - 예를 들어 (
    """
    e_list = [(e, i) for i, (m,e) in enumerate(list)]
    e_list.sort(key=lambda x: x[0], reverse=True)

    ret = 0
    begin_eat = 0
    for e, i in e_list:
        box = i
        begin_eat += list[box][0]
        ret = max(ret, begin_eat + list[box][1])

    return ret


# (m, e) : m(데우기), e(먹기)
data_list = [(1, 1), (2, 2), (3, 1)]
print(heat(data_list))

data_list = [(1, 3), (2, 4), (3, 3)]
print(heat(data_list))
