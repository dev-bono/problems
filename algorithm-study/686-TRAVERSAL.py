"""
전위순회, 중위순회 값을 주어주고
후위순회 방문순서를 구하라?
"""


def post_order(pre_order, in_order):

    if pre_order is None or len(pre_order) == 0:
        return ""
    root = pre_order[0]

    root_index = in_order.index(root)
    l_count = root_index
    # r_count = len(in_order) - root_index - 1

    post_order(pre_order[1:l_count+1], in_order[0:l_count])
    post_order(pre_order[l_count+1:], in_order[l_count+1:])

    print(root)


pre_order_list = [27, 16, 9, 12, 54, 36, 72]
in_order_list = [9, 12, 16, 27, 36, 54, 72]

post_order(pre_order_list, in_order_list)
