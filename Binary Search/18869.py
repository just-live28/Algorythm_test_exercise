from itertools import combinations
from bisect import bisect_left

m, n = map(int, input().split())
arr = []
for _ in range(m):
    line = list(map(int, input().split()))
    sorted_line = sorted(list(set(line)))
    
    planet = []
    for i in range(n):
        planet.append(bisect_left(sorted_line, line[i]))
    
    arr.append(planet)
    
result = 0
for planet1, planet2 in combinations(arr, 2):
    if planet1 == planet2:
        result += 1

print(result)