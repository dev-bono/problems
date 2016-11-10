"""
중간값들의 합 구하기
파이썬의 sort함수를 이용하면 쉽다
다양한 방법이 있는듯

"""


def median(n, a, b):
    """
     마지막 예제가 느림
    :param n:
    :param a:
    :param b:
    :return:
    """
    A = list()
    A.append(1983)
    ret_sum = 1983

    for i in range(1, n):
        A.append((A[i-1] * a + b) % 20090711)

        sorted_A = sorted(A)
        ret_sum += sorted_A[int((len(sorted_A)-1)/2)]

    return ret_sum % 20090711


print(median(10, 1, 0))
print(median(10, 1, 1))
print(median(10000, 1273, 4936))
