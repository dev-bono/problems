
"""
TODO: 무한루프에 빠지고 있음, 개선해야함.

H : row length
W : col length
R : 블럭 모양의 row length
C : 브럭 모양의 col length

1. 왼쪽위부터 순환
2. 채워져 있으면 다음 칸으로 이동
3. 비워져 있을때는 블럭 모양을 돌려가면서 채워지는 경우와 채워지지 않는 경우를 모두 체크한뒤
4. 다음칸으로 이동
5. max count return
"""
from copy import deepcopy

BASE = [
    [True, True, False, True, True, False, False],
    [True, False, False, False, False, False, False],
    [True, False, False, False, False, True, True],
    [True, False, False, True, True, False, False]
]

BLOCK = [
    [True, True, True],
    [True, False, False]
]

H = 4
W = 7
R = 2
C = 3


def rotate(block):
    return block


def fit_block(block, h_i, w_i):
    b_row_count = len(block)
    b_col_count = len(block[0])

    # print("row : ", h_i + b_row_count)
    # print("col : ", w_i + b_col_count)

    if h_i + b_row_count > H or w_i + b_col_count > W:
        return False

    for br_idx, b_row in enumerate(block):
        for bc_idx, c in enumerate(b_row):
            if BASE[br_idx + h_i][bc_idx + w_i]:
                return False
    return True


def get_next_idx(h, w):
    if w+1 == W:
        return h+1, 0
    else:
        return h, w+1


def get_count(h_i, w_i):
    ret_count = 0
    max_count = 0

    # 마지막이면, 끝
    if h_i == H-1 and w_i == W-1:
        return 0

    # 마지막이 아닐고 칸이 차있는(True) 경우 다음꺼 진행
    if BASE[h_i][w_i]:
        next_h, next_w = get_next_idx(h_i, w_i)
        return get_count(next_h, next_w)

    # 빈칸일때
    else:
        # rotate 하면서 한번씩 처리, 시계방향으로 0, 90, 180, 270 총 네번
        block = deepcopy(BLOCK)

        for i in range(4):
            if fit_block(block, h_i, w_i):
                print("fit")
                for br_idx, b_row in enumerate(block):
                    for bc_idx, c in enumerate(b_row):
                        BASE[br_idx + h_i][bc_idx + w_i] = True
                next_h, next_w = get_next_idx(h_i, w_i)
                ret_count = 1 + get_count(next_h, next_w)

                for br_idx, b_row in enumerate(block):
                    for bc_idx, c in enumerate(b_row):
                        BASE[br_idx + h_i][bc_idx + w_i] = False
            else:
                print("not fit")
                next_h, next_w = get_next_idx(h_i, w_i)
                ret_count = get_count(next_h, next_w)

            if ret_count > max_count:
                max_count = ret_count
            block = rotate(block)

        return max_count


get_count(0, 0)
