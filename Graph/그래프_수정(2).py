import heapq

# outdegree 기반 위상 정렬 함수
def topological_sort():
    max_heap = []
    for i in range(1, n+1):
        # 차수가 0인 노드를 큐에 추가
        if outdegree[i] == 0:
            heapq.heappush(max_heap, -i)
    
    NUM = n   # 현재 부여할 숫자
    while max_heap:
        now = -heapq.heappop(max_heap)
        result_sequence[now] = NUM
        NUM -= 1
        
        for nxt in graph[now]:
            outdegree[nxt] -= 1
            # 인접 노드의 차수가 0이 된 경우 큐에 추가
            if outdegree[nxt] == 0:
                heapq.heappush(max_heap, -nxt)

n = int(input())
outdegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    line = input()
    for j in range(1, n+1):
        # i → j라면 반대로 i의 차수를 올리고, j의 인접 노드에 i를 추가
        if line[j-1] == '1':
            outdegree[i] += 1
            graph[j].append(i)

# 결과 수열 초기화 및 위상 정렬 수행
result_sequence = [0] * (n+1)
topological_sort()

# 결과 수열에 0이 있다면 사이클(그래프를 수정할 수 없는 경우)이므로 -1 출력
if result_sequence[1:].count(0) > 0:
    print(-1)
# 결과 수열 출력
else:
    for i in result_sequence[1:]:
        print(i, end=' ')