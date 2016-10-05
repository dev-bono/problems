
# 오버플로우를 방지하기 위한 변수
MOD = 1000000007
cache = [-1] * 101


def tiling(width):
    """
    2 * n 크기의 사각형을 타일로 덮는 방법을 반환
    :param width:
    :return:
    """
    if width <= 1:
        return 1

    ret = cache[width]
    if ret != -1:
        return ret

    ret = (tiling(width-1) + tiling(width-2)) % MOD
    cache[width] = ret
    return ret


def asymmetric(width):
    """
    2 * n 크기의 사각형을 타일로 덮는 방법 중 가로로 비대칭인 경우의 수만 반환
    => 전체에서 대칭인 경우를 빼면 됨
    각 연산에서 MOD를 더해주는 이유는 뺀 결과값이 음수가 나올수도 있기 때문
    :param width:
    :return:
    """
    # 가로가 홀수이면 정가운데를 세로로 배치하는 방법밖에 없다. 그러므로 (width-1)/2개의 경우의수 구하면 됨
    if width % 2 == 1:
        return (tiling(width) - tiling(int((width-1)/2)) + MOD) % MOD

    # 가로가 짝수인 경우에는 가운데에 가로로 두개가 놓여 있거나 아예 없거나 두가지 경우를 각각 더한값을 전체에서 빼준다.
    ret = tiling(width)
    ret = (ret - tiling(int(width/2)) + MOD) % MOD
    ret = (ret - tiling(int((width-2)/2)) + MOD) % MOD

    return ret


# 비대칭에 대한 캐시가 별도로 필요함
asym_cache = [-1] * 101


def asymmetric2(width):
    """
    두번째 방법
    비대칭인 방법을 무식하게 구한다, 양쪽 끝에 놓을 수 있는 경우의 수를 구해 각각에 대해서 재귀적으로 구함
    :param width:
    :return:
    """
    if width <= 2:
        return 0

    ret = asym_cache[width]
    if ret != -1:
        return ret

    ret = asymmetric2(width-2) % MOD
    ret = (ret + asymmetric2(width-4)) % MOD
    ret = (ret + tiling(width-3)) % MOD
    ret = (ret + tiling(width-3)) % MOD

    asym_cache[width] = ret
    return ret


print(asymmetric(2))
print(asymmetric(4))
print(asymmetric(92))

print(asymmetric2(2))
print(asymmetric2(4))
print(asymmetric2(92))
