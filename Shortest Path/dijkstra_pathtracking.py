import heapq
INF = int(1e9)

start = 'D'
graph = {'A': [('B', 3), ('C', 2)],
         'B': [('A', 3), ('D', 4)],
         'C': [('A', 2), ('D', 1), ('F', 1)],
         'D': [('B', 4), ('C', 1), ('E', 5), ('G', 2)],
         'E': [('D', 5)],
         'F': [('C', 1), ('G', 3)],
         'G': [('D', 2), ('F', 3)]
         }
distance = {'A': INF, 'B': INF, 'C': INF, 'D': INF, 'E': INF, 'F': INF, 'G': INF}
path = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': []}

def dijkstra(start):
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                path[i[0]] = [now]
            elif cost == distance[i[0]]:
                path[i[0]].append(now)

def path_tracking(end):
    if start == end:
        return [[start]]
    
    routes = []
    for prev in path[end]:
        for r in path_tracking(prev):
            routes.append(r + [end])
    
    return routes
    
dijkstra(start)
print("=== D → F 까지의 최단거리와 최단경로 ===")
print("최단거리:", distance['F'], ", 최단경로:", path_tracking('F'))