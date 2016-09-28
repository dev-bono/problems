first = [10, 20, 30, 1, 2]
second = [10, 20, 30]


"""
 lis 구하는 로직부터 먼저 구해본다
 [3, 6, 4, 7, 8, 2, 5] 라는 리스트가 있을때 첫번째 숫자를 먼저 택한 후
 나머지 리스트에서 첫번째 숫자보다 큰 숫자들만 추려서 list를 만들어 lis의 인자로 보낸다.
 재귀적으로 호출하다보면 각 부분증가수열의 숫자 개수가 나오는데 이것들의 최대값을 구하면 된다
"""
def lis(list):
    if len(list) == 0:
        return 0

    max_len = 0
    # 리스트 전체 수를 순환
    for l in list:
        c_list = [n for n in list[1:len(list)] if l < n]
        max_len = max(max_len, 1 + lis(c_list))

    return max_len


test_list = [3, 6, 4, 7, 8, 2, 5, 12, 21, 52, 2, 55, 1, 32, 1, 7, 2, 2, 5, 21, 22, 5, 12 ,215, 3, 12, 5]
print(lis(test_list))


A = [1, 2, 3]
B = [10, 20, 30]
n = 5
m = 3

def jlis(index_A, index_B):

    if index_A >= len(A) or index_B >= len(B):
        return

    max_len = 2
    a = A[index_A]
    b = B[index_B]
    max_element = max(a, b)

    for i in range(index_A+1, n):
        if max_element < A[i]:
            max_len = max(max_len, jlis(i, index_B) + 1)

    for j in range(index_B+1, m):
        if max_element < B[j]:
            max_len = max(max_len, jlis(index_A, j) + 1)

    return max_len


print(jlis(0, 0))




# def jlis(list):
