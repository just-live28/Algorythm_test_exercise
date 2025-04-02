graph = { 
    'A': ['B', 'C'], 
    'B': ['D'], 
    'C': ['E'], 
    'D': [], 
    'E': [] 
  }

def dfs(graph, start_node):
    visit = []
    stack = []
    
    stack.append(start_node)
    while stack:
        now = stack.pop()
        
        if now not in visit:
            visit.append(now)
            # 실제 DFS 순서와 맞게 하기 위해 역순으로 삽입
            stack.extend(reversed(graph[now]))
    
    return visit

print(*dfs(graph, 'A'))     # 출력 A B D C E