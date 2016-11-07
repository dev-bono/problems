"""
전형적인 링크드 리스트 문제
파이썬에서 링크드 리스트를 어떻게 구현해야 할까?
닥셔너리로 구현해본다.
key(index): {value, pointer} 이렇게 세개 정보가 있고
pointer는 다음에 오게될 key를 가리킨다.

이 문제에서는 단순히 몇번째 사람이냐만 중요하므로 key(몇번째 사람), value(포인터)로만 표현한다
우선 1부터 순서대로 key, value에 값을 넣는다.
ex) n = 3 이면, {1:2, 2:3, 3:1} 과 같이 만든다.
처음 죽을 사람(dead_person)을 1로 초기화한다.

2명이 남을때까지 while 문 loop 를 돌면서
죽을 사람 이전의 사람의 포인터를 죽을사람의 포인터로 변경한다. 죽을사람은 pop 해준다.
그 다음 k 만큼 리스트를 이동하여 다음에 죽을사람(next_person)을 추출해둔다
반복한다.
남은 두명을 출력해주면 끝

"""


def josephus(n, k):
    linked_list_dic = {i+1: ((i+1) % n)+1 for i in range(n)}
    dead_person = 1
    list_len = len(linked_list_dic)

    while list_len > 2:
        dead_person_pointer = linked_list_dic[dead_person]
        linked_list_dic.pop(dead_person)
        pre_person = [k for k, v in linked_list_dic.items() if v == dead_person][0]
        linked_list_dic[pre_person] = dead_person_pointer
        list_len -= 1

        next_person = dead_person_pointer
        for j in range(k-1):
            next_person = linked_list_dic[next_person]

        dead_person = next_person

    return linked_list_dic.keys()


print(josephus(6, 3))
print(josephus(40, 3))

"""
두번째 방법
"""
def solve(list, k):
    die_index = 0
    while len(list) > 2:
        del list[die_index]
        die_index -= 1
        die_index = (die_index + k) % len(list)
    return list

print(solve([1,2,3,4,5,6], 3))

list = [i+1 for i in range(40)]
print(solve(list, 3))
        
