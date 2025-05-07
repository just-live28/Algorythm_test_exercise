import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# N 정점 수 R 루트 번호 Q 쿼리 수
N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

tree = [[-1, []] for _ in range(N+1)]
size = [0] * (N+1)

def make_tree(cur, parent):
    for node in graph[cur]:
        if node == parent:
            continue
        tree[cur][1].append(node)
        tree[node][0] = cur
        make_tree(node, cur)

def count_subtree_nodes(cur):
    size[cur] = 1
    for node in tree[cur][1]:
        count_subtree_nodes(node)
        size[cur] += size[node]
    
make_tree(R, -1)
count_subtree_nodes(R)
for _ in range(Q):
    num = int(input())
    print(size[num])