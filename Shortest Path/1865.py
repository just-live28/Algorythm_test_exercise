tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())

    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    distance = [0] * (n+1)
    cycle = False
    for i in range(n):
        for st, en, dist in edges:
            if distance[st] + dist < distance[en]:
                distance[en] = distance[st] + dist

                if i == n-1:
                    cycle = True
                    break

    if cycle:
        print('YES')
    else:
        print('NO')