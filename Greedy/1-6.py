food_times = [3,1,2]
k = 5

import heapq

def solution(food_times, k):
    q = []
    total_time = 0
    for i in range(1, len(food_times) + 1):
        heapq.heappush(q, (food_times[i-1], i))
        total_time += food_times[i-1]
    
    if total_time <= k:
        return -1
    
    remain_time = k
    prev = 0
    while (q[0][0] - prev) * len(q) <= remain_time:
        remain_time -= (q[0][0] - prev) * len(q)
        prev = heapq.heappop(q)[0]
    
    remain_foods = []
    while q:
        remain_foods.append(heapq.heappop(q)[1])
    
    remain_foods.sort()
    return remain_foods[remain_time % len(remain_foods)]
        
        
print(solution(food_times, k))