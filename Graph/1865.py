import sys
input = sys.stdin.readline
INF = int(1e9)

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    for i in range(1, n+1):
        edges.append((0, i, 0))
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    distance = [INF] * (n+1)
    distance[0] = 0

    cycle = False
    for i in range(n):
        for j in range(len(edges)):
            cur, nxt, cost = edges[j]

            if distance[cur] != INF and distance[cur] + cost < distance[nxt]:
                distance[nxt] = distance[cur] + cost

                if i == n-1:
                    cycle = True

    if cycle:
        print('YES')
    else:
        print('NO')