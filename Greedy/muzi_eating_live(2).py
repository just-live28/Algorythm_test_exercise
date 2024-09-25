import heapq

# 1초마다 하나의 음식 섭취
# k초 후에 방송장애 / 이후 먹어야할 음식의 인덱스 (없다면(=다먹었다면) -1)

# heapq에 저장 (남은시간, 음식번호)
# 큐에서 꺼내 남은시간이 k에 도달하지 않는다면 그 음식을 섭취하고 섭취변수(ate_time)에 그 시간을 추가
# 다음 큐에서 꺼낸 남은시간은 ate_time을 빼줘야한다. 그 시간이 k에 도달하지 않는다면 동일하게 처리
# k에 도달한다면.. 큐의 각 항목의 음식번호만 추출하여 리스트에 담고, k와 리스트 개수를 조합하여 답을 구한다.

# 1 1*3s
# 1 

food_times = [3, 1, 2]
k = 5

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    foods = []
    for i in range(len(food_times)):
        heapq.heappush(foods, (food_times[i], i+1))

    total = 0
    prev = 0
    length = len(foods)
    while(total + length * (foods[0][0] - prev) <= k):
        now = heapq.heappop(foods)[0]
        ate = now - prev

        total += length * ate
        length -= 1
        prev = now

    foods.sort(key = lambda x : x[1])

    index = (k- total) % length
    return foods[index][1]

print(solution(food_times, k))