
# 그래프의 인접 행렬 표현 adj[i][j] = i 와 j 사이 간선의 수
adj = []
# graph[i][j] = i 로 시작해서 j 로 끝나는 단어의 목록
graph = []
# indegree[i] = i 로 시작하는 단어의 수
indegree = []
# outdegree[i] = i 로 끝나는 단어의 수
outdegree = []


def make_graph(words):
    """
    그래프 초기화 및 생성
    :param words:
    :return:
    """
    global graph, adj, indegree, outdegree

    # 초기화
    graph = [[-1 for j in range(26)] for i in range(26)]
    adj = [[0 for j in range(26)] for i in range(26)]
    indegree = [0 for i in range(26)]
    outdegree = [0 for i in range(26)]

    # 단어 입력
    # a 로 시작하고 b 로 끝나는 단어를 graph[a][b]에 저장한다.
    for i in range(len(words)):
        a = ord(words[i][0]) - ord('a')   # 시작 문자 index
        b = ord(words[i][len(words[i])-1]) - ord('a')   # 종료 문자 index
        graph[a][b] = words[i]
        # a 와 b 사시의 간선수 +1
        adj[a][b] += 1
        # a 로 끝나는 단어수 +1, 이 노드(a)에서 다른 노드로 나가는 edge(단어) 가 1개 있다는 것
        outdegree[a] += 1
        # b 로 시작하는 단어수 +1, 이 노드(b)로 들어오는 edge(단어) 가 1개 있다는 것
        indegree[b] += 1


def get_euler_circuit(here, circuit):
    """
    간선수(adj)를 이용하여 오일러 서킷 또는 트레일 계산
    모든 간선을 돌면서 0이 될때까지 진행
    들어오고(here) 나가는(there)를 바꿔가면서 재귀적으로 진행
    :param here:
    :param circuit:
    :return:
    """
    global adj
    for there in range(len(adj)):
        # 두 점 (here, there) 사이에 간선이 존재한다면,
        while adj[here][there] > 0:
            adj[here][there] -= 1
            get_euler_circuit(there, circuit)

    # 들어온 지점(알파벳)은 circuit 리스트에 하나씩 붙여준다.
    circuit.append(here)


def get_euler_trail_or_circuit():
    """
    outdegree, indegree 값을 바탕으로 들어오고 나오는 값을 비교하여 트레일을 찾을 수 있는지 먼저 검사한다.
    트레일이 가능한 지점이라면 circuit을 찾는다.

    트레일이 불가능한 경우에는 나가는 지점(outdegree)를 돌면서 하나씩 찾는다.

    어차피 하나만 찾으면 되므로 찾게되면 그냥 리턴

    :return:
    """
    global outdegree, indegree
    circuit = []

    # 우선 트레일을 찾아본다.
    for i in range(26):
        # outdegree(나가는게)가 1 더 큰 지점은 시작점이므로 시작점을 기준으로 오일러 트레일 검사
        if outdegree[i] == indegree[i]+1:
            get_euler_circuit(i, circuit)
            return circuit

    # loop 를 돌면서 오일러 서킷 검사
    for j in range(26):
        if outdegree[j]:
            get_euler_circuit(j, circuit)
            return circuit

    # 모두 실패하면 빈 배열
    return circuit


def check_euler():
    """
    outdegree, indegree 를 바탕으로 오일러 서킷/트레일이 가능한지 검사
    :return:
    """
    global outdegree, indegree
    plus1 = 0
    minus1 = 0
    for i in range(26):
        # 해당 노드 i에서 나가고(out) 들어오는(in) 값의 차이, delta가 -1(끝)/1(시작)이면 트레일 가능성
        delta = outdegree[i] - indegree[i]
        if delta < -1 or delta > 1:
            return False
        if delta == 1:
            plus1 += 1
        if delta == -1:
            minus1 += 1

    # plus1 과 minus1 이 각각 1이라면 시작점과 끝점이 하나씩 존재한다는 것이기 때문에 트레일이 가능하다는 말과 같다.
    # plus1 과 minus1 이 0인 경우에는 서킷 형태
    return (plus1 == 1 and minus1 == 1) or (plus1 == 0 and minus1 == 0)


def solve(words):
    global graph
    make_graph(words)

    if not check_euler():
        return "IMPOSSIBLE"

    # circuit(시작부터 끝까지의 알파벳 리스트)는 반드시 words 보다 한개 많아야 한다.
    # ex) dog god dragon need
    # circuit = [d, g, d, n, d]
    circuit = get_euler_trail_or_circuit()
    if len(circuit) != len(words) + 1:
        return "IMPOSSIBLE"

    ret = ""
    # 왜 reverse 하는 거지??? 아마 처음부터 반대로 들어갔을거 같은데 어느지점인지 모르겠네
    circuit.reverse()
    # 맨 처음 시작점(끝점)은 필요없으니 제외하고 순회
    for i in range(1, len(circuit)):
        a = circuit[i-1]
        b = circuit[i]
        if len(ret):
            ret += " "

        # a로 시작하고 b로 끝나는 단어를 추가해준다.
        ret += graph[a][b]
        # 초기화 해줌
        graph[a][b] = -1

    return ret

p1 = ['dog', 'god', 'dragon', 'need']
p2 = ['aa', 'ab', 'bb']
p3 = ['ab', 'cd']

print(solve(p1))
print(solve(p2))
print(solve(p3))

