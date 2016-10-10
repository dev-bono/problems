"""
- 왼쪽 또는 오른쪽의 한 숫자를 가져갈 수 있다, 가져가면 없어짐
- 숫자가 2개 이상일 때 왼쪽 또는 오른쪽의 숫자를 지울수 있다
- 경우의 수가 4개이므로 각각의 경우에 대해서 가능한 방법을 모두 해보면 되지 않을까??
- play()는 Max(자신-상대점수)
- 즉 숫자가 음수일때는 최대한 버리고, 양수일때는 취하는게 이득
"""


class Board:
    EMPTY = -987654321
    cache = None

    def __init__(self, board):
        self.board = board
        l = len(board)
        self.cache = [[self.EMPTY] * l for x in range(l + 1)]

    def play(self, left, right):
        if left > right:
            return 0

        diff_max = self.cache[left][right]
        if diff_max != self.EMPTY:
            return diff_max

        # 왜 - play(left-1, right)냐면, 다음 플레이는 상대방의 최대값이 될것이기 때문이다.
        diff_max = max(self.board[left] - self.play(left+1, right), self.board[right] - self.play(left, right-1))

        if right >= left + 1:
            diff_max = max(diff_max, -self.play(left+2, right), -self.play(left, right-2))

        self.cache[left][right] = diff_max
        return diff_max


board = [-1000, -1000, -3, -1000, -1000]
b = Board(board)
print(b.play(0, 4))

board = [100, -1000, -1000, 100, -1000, -1000]
b = Board(board)
print(b.play(0, 5))

board = [7, -5, 8, 5, 1, -4, -8, 6, 7, 9]
b = Board(board)
print(b.play(0, 9))
