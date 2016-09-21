
# [0,0]은 기준점 [아래, 우측] 증가
cover_type = [
    [[0, 0], [1, 0], [0, 1]],
    [[0, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [1, -1]],
]

board = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]


# y, x 가장 왼쪽 상단 지점
def set(board, y, x, type, delta):
    ok = True
    for i in range(3):
        # 타입에 따라 한칸씩 이동
        ny = y + cover_type[type][i][0]
        nx = x + cover_type[type][i][1]
        # 밖으로 나갔으면 False
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok = False
        # 이미 덮여져 있는 경우
        else:
            board[ny][nx] += delta
            if board[ny][nx] > 1:
                # delta가 1인경우 기존에 덮여져 있어도 1 추가함 왜냐하면 이후에 블록을 치울때 잘못된 경우에도 -1 해줘야 하므로
                ok = False

    return ok


def cover(board):
    ret = 0
    y = x = -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            # 비어 있다면,
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break

    if y == -1:
        return 1

    for type in range(4):
        # type 형태로 덮을수 있는면 채운뒤 다른 블록
        if set(board, y, x, type, 1):
            ret += cover(board)

        # 덮었던 블록 치우기
        set(board, y, x, type, -1)

    return ret

print(cover(board))