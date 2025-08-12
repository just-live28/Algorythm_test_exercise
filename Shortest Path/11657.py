# n-1 번 만큼 반복
# 모든 간선에 대해, dist 갱신이 가능하면 갱신
# n번째 수행에서, 갱신이 일어나면 음의 사이클 존재
INF = int(1e9)

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bellman_ford(start, edges, n):
    distance = [INF] * (n+1)
    distance[start] = 0

    for i in range(n):
        updated = False
        for st, en, dist in edges:
            if distance[st] != INF and distance[st] + dist < distance[en]:
                updated = True
                distance[en] = distance[st] + dist
        
        if not updated:
            break
        elif i == n-1 and updated:
            return []
    
    return distance

distance = bellman_ford(1, edges, n)
if not distance:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])