"""
몇번을 더 이기면 승률이 높아지는지를 찾는문제
ex.
- 현재 10번중 8번을 이겻다면, 승률이 80%이다
- 81%가 되려면 몇번을 이겨야 할까?
- 1번 더 이겨서 11번중 9번을 이겼다면 81%가 되므로 정답은 1

20억이 max이므로, 절반씩 줄여나간다.
"""

L = 2000000000


def ratio(g, w):
    return int(w*100/g)


def needed_games(games, won):
    # 20억번을 해도 수치가 같다면 -1 리턴
    if ratio(games, won) == ratio(games+L, won+L):
        return -1

    hi = L
    lo = 0

    while lo+1 < hi:
        mid = int((hi + lo) / 2)
        # 앞 구간에서 승률이 올랐다.
        if ratio(games, won) < ratio(games+mid, won+mid):
            hi = mid
        # 앞 구간에서 승률이 오르지 않았다.
        else:
            lo = mid

    return hi


print(needed_games(100, 80))
print(needed_games(47, 47))
print(needed_games(99000, 0))
print(needed_games(1000000000, 470000000))
