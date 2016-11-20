# 정점수
n = 10

visited = [False] * n
adj = [[1], [2, 3, 6], [4], [5, 7], [], [], [], []]


def dfs(here):
    visited[here] = True
    print("{} ".format(here))

    for a in adj[here]:
        there = a
        if not visited[there]:
            dfs(there)


def dfs_all():
    for i in range(len(adj)):
        if not visited[i]:
            dfs(i)

dfs_all()

