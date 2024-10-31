import heapq

food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    if sum(food_times) < k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    ate_time = 0
    while(True):
        if ate_time + q[0][0] * len(q) > k:
            break
        
        time, index = heapq.heappop(q)        
        
        ate_time += time * (len(q) + 1)
    
    foods = []
    while(q):
        time, index = heapq.heappop(q)
        foods.append(index)
    foods.sort()
    
    idx = (k - ate_time) % len(foods)
    return foods[idx]

print(solution(food_times, k))
    
            
    
    
    