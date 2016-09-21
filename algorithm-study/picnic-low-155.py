
# 가장 낮은 숫자의 친구부터 시작한다

# 4 6
# 01 12 23 30 02 13
# 01 23
# 02 13
# 03 12

# 6 10
# 01 02 12 13 14 23 24 34 35 45
# 01 23 45
# 01 24 35
# 02 13 45
# 02 14 35

pair_list = [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]
num = 6
friend = [[False for j in range(num)] for i in range(num)]


def insert_friend(pairs):
    for p in pairs:
        friend[p[0]][p[1]] = True
        friend[p[1]][p[0]] = True


# 우선 낮은수부터 한쌍을 구한뒤 나머지로 계속 구하다 남은 친구 없으면 카운팅 있으면 return 0
def count_pair(remains):
    ret_count = 0

    free_first = -1
    # 짝이 없는 가장 빠른 친구 찾기
    for i in range(num):
        if not remains[i]:
            free_first = i
            break;

    # 친구가 남았는지부터 확인해야겠지 없으면 return 1
    if free_first == -1:
        return 1

    for pair_with in range(free_first+1, num):
        if not remains[pair_with] and friend[free_first][pair_with]:
            remains[free_first] = remains[pair_with] = True
            ret_count += count_pair(remains)
            # 다시 세야하니깐 초기화
            remains[free_first] = remains[pair_with] = False

    return ret_count


insert_friend(pair_list)

remains = [False for i in range(num)]
print(count_pair(remains))

