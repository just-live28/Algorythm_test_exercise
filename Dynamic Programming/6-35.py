# import heapq

# q = []
# heapq.heappush(q, 1)

# array = set()
# array.add(1)

# n = int(input())

# while len(array) < n:
#     num = heapq.heappop(q)
#     array.add(num)
    
#     heapq.heappush(q, 2 * num)
#     heapq.heappush(q, 3 * num)
#     heapq.heappush(q, 5 * num)

# array = sorted(array)
# print(array[-1])

index2, index3, index5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5

ugly = []
ugly.append(1)

n = int(input())

for _ in range(n-1):
    ugly.append(min(next2, next3, next5))
    
    if ugly[-1] == next2:
        index2 += 1
        next2 = ugly[index2] * 2
    if ugly[-1] == next3:
        index3 += 1
        next3 = ugly[index3] * 3
    if ugly[-1] == next5:
        index5 += 1
        next5 = ugly[index5] * 5

print(ugly[-1])