# 간선마다 양방향 연결
# 큐에서 노드를 빼오고, 해당 노드와 연결된 자식 노드들을 순회
# 각 자식 노드의 부모 노드가 -1(미방문 상태)이라면 해당 노드를 부모 노드로 설정하고, 큐에 자식 노드를 추가
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

parent = [-1] * (n+1)
parent[1] = 1
while q:
    now = q.popleft()
    
    for i in graph[now]:
        if parent[i] == -1:
            parent[i] = now
            q.append(i)

for i in parent[2:]:
    print(i)